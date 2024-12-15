
from functools import reduce
from Day.day import Day

part2_file = ".\\src\\Day2\\input.txt"

class Day2(Day):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self):
        reports = _get_reports()
        reportsCopy = reports[:]
        print("Safe Levels: " + str(reduce(lambda x, y: x + y.is_safe(), reports, 0)))
        print("Safe Levels with Dampener: " + str(reduce(lambda x,y: x + y.is_safe_dampener(), reportsCopy, 0)))

class Report():
    def __init__(self, levels: list[int]) -> None:
        self.levels = levels
    
    def is_safe(self) -> bool:
        if self.levels[0] < self.levels[1]:
            return _safe_increasing(self.levels)
        elif self.levels[0] > self.levels[1]:
            return _safe_increasing(self.levels[::-1])
        else:
            return False
    
    def is_safe_dampener(self) -> bool:
        flippedLevels = self.levels[::-1]
        return _safe_increasing_dampener2(self.levels,0) or _safe_increasing_dampener2(flippedLevels,0)

def _get_reports() -> list[Report]:
    reports: list[Report] = []
    with open(part2_file, "r") as file:
        for line in file:
            line = line.split()
            reports.append(Report(list(map(int,line))))
    
    return reports

def _safe_increasing(levels: list[int]) -> bool:
    if len(levels) == 1:
        return True
    
    if not (0 < (levels[1] - levels[0]) <= 3):
        return False
    
    return True and _safe_increasing(levels[1:])

def _safe_increasing_dampener(levels: list[int], removals: int) -> bool:
    if removals > 1:
        return False

    if len(levels) == 1:
        return True
    
    if not (0 < (levels[1] - levels[0]) <= 3):
        removezero = _safe_increasing_dampener(levels[1:], removals + 1)
        
        levels.pop(1)
        return removezero or _safe_increasing_dampener(levels, removals + 1)
    
    return True and _safe_increasing_dampener(levels[1:], removals)

def _safe_increasing_dampener2(levels: list[int], removals: int) -> bool:
    if removals > 1:
        return False
    
    if len(levels) == 1:
        return True
    
    for num in range(len(levels) - 1):
        if not (0 < levels[num + 1] - levels[num] <= 3):
            copyWithoutThis = levels[:]
            copyWithoutThis.pop(num)

            copyWithoutThat = levels[:]
            copyWithoutThat.pop(num + 1)

            return _safe_increasing_dampener2(copyWithoutThis, removals + 1) or _safe_increasing_dampener2(copyWithoutThat, removals + 1)
        else:
            continue
    
    return True


    