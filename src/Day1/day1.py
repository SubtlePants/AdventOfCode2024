
from functools import reduce
from Day.day import Day

part1_file = '.\\src\\Day1\\input.txt'


class Day1(Day):
    def __init__(self, ) -> None:
        super().__init__()
    
    def run(self) -> None:
        (list1, list2) = _read_two_lists_from_url()
        print("Distance= " +  str(_two_list_distance(list1, list2)))
        print("Similarity= " + str(_two_list_similarity(list1, list2)))


def _two_list_distance(list1: list[int], list2: list[int]) -> int:
    list1.sort()
    list2.sort()

    merged_list = list(map(lambda x, y:(x,y), list1, list2))

    return reduce(lambda x, y: x + abs(y[0] - y[1]), merged_list, 0 )

def _two_list_similarity(list1: list[int], list2: list[int]) -> int:
    list2occurences: dict[int, int] = {}
    for number in list2:
        try:
             list2occurences[number] = list2occurences[number] + 1
        except:
            list2occurences[number] = 1
    return reduce(lambda x,y: x + (y * _list_two_occurance(list2occurences, y)), list1, 0)

def _list_two_occurance(occurances: dict[int, int], number: int):
    try:
        return occurances[number]
    except:
        return 0

def _read_two_lists_from_url() -> tuple[list[int], list[int]]:
    lists: tuple[list[int], list[int]] = ([], [])

    with open(part1_file, 'r') as file:
        for line in file:
            numbers = line.split()
            lists[0].append(int(numbers[0]))
            lists[1].append(int(numbers[1]))
    
    return lists
