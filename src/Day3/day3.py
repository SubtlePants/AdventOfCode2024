
from functools import reduce
from Day.day import Day
from re import findall

part3_file = ".\\src\\Day3\\input.txt"


class Day3(Day):
    def __init__(self) -> None:
        with open(part3_file, "r") as file:
            self.input = file.read()
            self.input.split()
    
    def run(self):
        mulStrings: list[str] = findall("mul\\([0-9]+,[0-9]+\\)", self.input)
        intTuplesToMultiply: list[tuple[int, int]] = list(map(_turn_mult_string_into_num_tuples, mulStrings))
        part1result = reduce(lambda y, x: y + (x[0] * x[1]), intTuplesToMultiply, 0)
        print(part1result)

        codeStrings: list[str] = findall("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)", self.input)
        print(_execute_do_dont_mult_code(codeStrings))


def _turn_mult_string_into_num_tuples(multstring: str) -> tuple[int,int]:
    numbers: list[str] = findall("[0-9]+", multstring)
    return (int(numbers[0]), int(numbers[1]))

def _execute_do_dont_mult_code(codestrings: list[str]) -> int:
    result = 0
    do: bool= True
    for command in codestrings:
        if command == "do()":
            do = True
            continue
        if command == "don't()":
            do = False
            continue
        if not do:
            continue
        # else do
        multnumbers = _turn_mult_string_into_num_tuples(command)
        result += multnumbers[0] * multnumbers[1]
    
    return result




