
from Day1.day1 import Day1
from Day2.day2 import Day2
from Day3.day3 import Day3
from Day4.day4 import Day4
from Day5.day5 import Day5
from Day6.day6 import Day6

day= int(input("Which Day? "))

match day:
    case 1:
        Day1().run()
    case 2:
        Day2().run()
    case 3:
        Day3().run()
    case 4:
        Day4().run()
    case 5:
        Day5().run()
    case 6:
        Day6().run()
    case _:
        raise IOError("Not a valid day")