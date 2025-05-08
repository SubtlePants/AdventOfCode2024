
from functools import cmp_to_key
from math import floor
from Day.day import Day

part5_file = ".\\src\\Day5\\input.txt"


class Day5(Day):
    def __init__(self) -> None:
         self.rules: list[tuple[int,int]] = []
         self.updates: list[list[int]] = []
         self.rules_allowing: dict[int,list[int]] = {}
         self.allowed_dictionary: dict[int,bool] = {}
         self.fancy_dict: dict[tuple[int,int], int] = {}
         with open(part5_file, "r") as file:
            file = file.read()
            lines = file.split(sep="\n")
            for line in lines:
                if "|" in line:
                    rule = line.split(sep="|")
                    self.rules.append((int(rule[0]), int(rule[1])))
                elif "," in line:
                    update = [int(n) for n in line.split(sep=",")]
                    self.updates.append(update)
                else:
                    continue
            
            for rule in self.rules:
                self.fancy_dict[rule] = -1
                if not rule[1] in self.rules_allowing:
                    self.rules_allowing[rule[1]] = [rule[0]]
                else:
                    self.rules_allowing[rule[1]].append(rule[0])
                
                self.allowed_dictionary[rule[1]] = True

    
    def run(self):
        print("Running day 5...")
        
        total_of_correct_middle_pages = 0
        total_of_fixed_middle_pages = 0
        for update in self.updates:
            fixed_update = self._fix_update(update)
            if update == fixed_update:
                total_of_correct_middle_pages += self._get_middle_page(update)
            else:
                total_of_fixed_middle_pages += self._get_middle_page(fixed_update)
        
        print("The total of already correct middle pages is " + str(total_of_correct_middle_pages))
        print("The total of fixed middle pages is " + str(total_of_fixed_middle_pages))
    
    def _fix_update(self, update:list[int]) -> list[int]:
        update_copy = update.copy()
        cmp = cmp_to_key(self._comparison_function)
        fixed_update = sorted(update_copy,key=cmp)
        return fixed_update
    
    def _comparison_function(self, x:int, y:int):
        return self.fancy_dict.get((x,y), 0)

    
    def _get_middle_page(self, update:list[int]) -> int:
        return update[floor((len(update)-1)/2)]