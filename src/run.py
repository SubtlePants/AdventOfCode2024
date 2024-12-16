
from Day1.day1 import Day1
from Day2.day2 import Day2
from Day3.day3 import Day3

day= int(input("Which Day? "))

match day:
    case 1:
        Day1().run()
    case 2:
        Day2().run()
    case 3:
        Day3().run()
    case _:
        raise IOError("Not a valid day")