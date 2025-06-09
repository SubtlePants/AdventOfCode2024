

from Day.day import Day

part6_file = ".\\src\\Day6\\input_test.txt"


class Day6(Day):
    def __init__(self) -> None:
        map: list[list[Terrain]] = []
        guard_coord: tuple[int,int] = (0,0)
        with open(part6_file) as file:
            file = file.read()
            lines = file.split("\n")
            for i in range(len(lines)):
                char_list = list(lines[i])
                terrain_list:list[Terrain] = []
                for j in range(len(char_list)):
                    if char_list[j] == ".":
                        terrain_list.append(Terrain(True))
                    if char_list[j] == "#":
                        terrain_list.append(Terrain(False))
                    if char_list[j] == "^":
                        terrain_list.append(Terrain(True))
                        guard_coord = (i,j) # i think the inverted coords here are correct if top left is (0,0)
                        print(guard_coord)
                map.append(terrain_list)

        self.guard = Guard(guard_coord, (-1,0), map)
    
    def run(self):
        print("Running Day 6")
        while True:
            try:
                self.guard.move()
            except IndexError:
                print("I am out of bounds")
                break
        
        print("Visited " + str(len(self.guard.squares_visited)) + " squares")
        print("Possible obstacles placed for looping is " + str(self.guard.possible_loops))

class Terrain():
    def __init__(self, walkable:bool) -> None:
        self.walkable = walkable


class Guard():
    def __init__(self, coord: tuple[int,int], direction:tuple[int,int], map:list[list[Terrain]]) -> None:
        self.coord = coord
        self.direction: tuple[int,int] = direction
        self.squares_visited: dict[tuple[int,int], list[tuple[int,int]]] = {coord: [direction]}
        self.possible_loops = 0
        self.map= map
    
    #(0,-1)->(1,0)->(0,1)->(-1,0)-> (x,y) -> (y,-x)
    def _turn_right(self):
        self.direction = self._get_direction_to_right()

    def move(self):
        (dest_x,dest_y) = tuple(i+j for i, j in zip(self.coord, self.direction))

        if dest_x < 0 or dest_y < 0:
            raise IndexError
        
        if not self.map[dest_x][dest_y].walkable:
            self._turn_right()
            return

        self.coord = (dest_x,dest_y)

        #calc potential looping with block
        if self.coord in self.squares_visited and self._get_coord_to_right() in self.squares_visited:
            if self._get_direction_to_right() in self.squares_visited[self._get_coord_to_right()]:
                print(self._get_direction_to_right())
                print(self._get_coord_to_right())
                print(self.squares_visited[self._get_coord_to_right()])
                print("Blocking Barrel at " + str(tuple(i+j for i, j in zip(self.coord, self.direction))))
                self.possible_loops += 1

        if self.coord not in self.squares_visited:
            self.squares_visited[self.coord] = [self.direction]
        else:
            self.squares_visited[self.coord].append(self.direction)
        
        print ("I am at " + str(self.coord) + " I am moving in this direction: " + str(self.direction))

    
    def _get_coord_to_right(self):
        right_direction = self._get_direction_to_right()
        (right_x, right_y) = tuple(i+j for i, j in zip(self.coord, right_direction))
        return (right_x, right_y)
    
    def _get_direction_to_right(self):
        (x, y) = self.direction
        return (y,-x)