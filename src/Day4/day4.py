

from Day.day import Day

part4_file = ".\\src\\Day4\\input.txt"


class Day4(Day):
    def __init__(self) -> None:
        with open(part4_file, "r") as file:
            file = file.read()
            self.input = file.split(sep="\n")

    def run(self):
        print("Running Day 4")

        xmas_count = 0
        for line_number in range(len(self.input)):
            for row_number in range(len(list(self.input[line_number]))):
                if list(self.input[line_number])[row_number] == "X":
                    xmas_count += _count_xmas(line_number, row_number, self.input)
        
        print("XMAS count is: " + str(xmas_count))

        x_mas_count = 0
        for line_number in range(len(self.input)):
            for row_number in range(len(list(self.input[line_number]))):
                if list(self.input[line_number])[row_number] == "A":
                    x_mas_count += int(_check_x_mas(line_number, row_number, self.input))
        
        print("X-MAS count is " + str(x_mas_count))

    
def _count_xmas(line_number:int, row_number:int, grid:list[str]) -> int:
    vectors = [(1,0), (0,1), (1,1), (-1,-1), (1,-1), (-1,1), (-1,0), (0,-1)]
    count = 0
    for vector in vectors:
        count += _count_xmas_direction((line_number, row_number), vector, grid)
    return count

def _count_xmas_direction(start:tuple[int,int], vector:tuple[int,int], grid:list[str]) -> int:
    m_coord = tuple(map(lambda i,j: i+j, start, vector))
    if m_coord[0] < 0 or m_coord[1] < 0:
        return 0
    a_coord = tuple(map(lambda i,j: i+j, m_coord, vector))
    if a_coord[0] < 0 or a_coord[1] < 0:
        return 0
    s_coord = tuple(map(lambda i,j: i+j, a_coord, vector))
    if s_coord[0] < 0 or s_coord[1] < 0:
        return 0
    try:
        if list(grid[m_coord[0]])[m_coord[1]] != "M":
            return 0
        if list(grid[a_coord[0]])[a_coord[1]] != "A":
            return 0
        if list(grid[s_coord[0]])[s_coord[1]] != "S":
            return 0
    except IndexError:
        return 0

    # print(str(start) + str(m_coord) + str(a_coord) + str(s_coord))
    return 1

def _check_x_mas(line_number:int, row_number:int, grid:list[str]):
    corner_pair_vectors_1 = [(-1,-1), (1,1)]
    corner_pair_vectors_2 = [(-1,1), (1,-1)]
    # corner_pair_letters_1 = reduce(_get_letter_from_vector((line_number, row_number), grid=grid), corner_pair_vectors_1)
    corner_letters_1 = _check_corner_letters((line_number,row_number),corner_pair_vectors_1,grid)
    corner_letters_2 = _check_corner_letters((line_number,row_number),corner_pair_vectors_2,grid)
    return corner_letters_1 and corner_letters_2

def _check_corner_letters(start:tuple[int,int], vectors:list[tuple[int,int]], grid:list[str]):
    corners: list[str] = []
    for vector in vectors:
        try:
            coord = tuple(map(lambda i,j: i+j, start, vector))
            if coord[0] < 0 or coord[1] < 0:
                return False
            corners.append(list(grid[coord[0]])[coord[1]])
        except IndexError:
            return False
    
    if "M" in corners and "S" in corners and len(corners) == 2:
        return True
    
    return False
