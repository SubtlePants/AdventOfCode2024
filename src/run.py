
from Day1.day1 import Day1
from Day2.day2 import Day2, _safe_increasing_dampener2

day= int(input("Which Day? "))

buggyLevels = [1,2,3,4,10,11]
print(_safe_increasing_dampener2(buggyLevels, 0))

match day:
    case 1:
        Day1().run()
    case 2:
        Day2().run()
    case _:
        raise IOError("Not a valid day")