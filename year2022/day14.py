'''
part1: #1942 31:16
part2: #3144 55:27

spent too long trying to get the padding right!
'''
from enum import Enum


with open("day14.in") as f:
    data = f.read().strip()

data = [[[int(y) for y in x.split(",")] for x in p.split(" -> ")] for p in data.split("\n")]

class Type(Enum):
    ROCK = "#"
    SAND = "+"
    AIR = " "

    def __repr__(self):
        return self.value

PADDING = 1000
min_x = float("inf")
max_x = -float("inf")
min_y = 0
max_y = -float("inf")

for row in data:
    for (x, y) in row:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)

grid1 = [[Type.AIR for _ in range(min_x - PADDING, max_x + 1 + PADDING)] for _ in range(min_y, max_y + 3)]
grid2 = [[Type.AIR for _ in range(min_x - PADDING, max_x + 1 + PADDING)] for _ in range(min_y, max_y + 3)]

for row in data:
    for i, (x_1, y_1) in enumerate(row):
        if i == 0:
            continue
        x_2, y_2 = row[i - 1]

        x_start = min(x_1, x_2)
        x_end = max(x_1, x_2)
        y_start = min(y_1, y_2)
        y_end = max(y_1, y_2)

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                grid1[y - min_y][x - min_x + PADDING] = Type.ROCK
                grid2[y - min_y][x - min_x + PADDING] = Type.ROCK

def add_tup(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))

START = (500 - min_x + PADDING, 0 - min_y)
DOWN = (0, 1)
LEFT = (-1, 1)
RIGHT = (1, 1)

def simulate1(grid) -> bool:
    curr = START
    while True:
        if curr[1] > max_y:
            return False

        down_ = add_tup(curr, DOWN)
        left_ = add_tup(curr, LEFT)
        right_ = add_tup(curr, RIGHT)

        if grid[down_[1]][down_[0]] == Type.AIR:
            curr = down_
        elif grid[left_[1]][left_[0]] == Type.AIR:
            curr = left_
        elif grid[right_[1]][right_[0]] == Type.AIR:
            curr = right_
        else:
            break

    grid[curr[1]][curr[0]] = Type.SAND
    return True

def simulate2(grid) -> bool:
    curr = START
    while True:
        if curr[1] == max_y + 1:
            break

        down_ = add_tup(curr, DOWN)
        left_ = add_tup(curr, LEFT)
        right_ = add_tup(curr, RIGHT)

        if grid[down_[1]][down_[0]] == Type.AIR:
            curr = down_
        elif grid[left_[1]][left_[0]] == Type.AIR:
            curr = left_
        elif grid[right_[1]][right_[0]] == Type.AIR:
            curr = right_
        else:
            break

    grid[curr[1]][curr[0]] = Type.SAND

    return curr != START

part1 = 0
while simulate1(grid1):
    part1 += 1

part2 = 1 # +1 because this loop skips counting the final sand
while simulate2(grid2):
    part2 += 1

print(f"part1: {part1}")
print(f"part2: {part2}")

'''
# change PADDING to 10 and print the sample data to get this! :)

for x in grid2:
    print(" ".join(map(repr, x)))

                                +                          
                              + + +                        
                            + + + + +                      
                          + + + + + + +                    
                        + + # + + + # # +                  
                      + + + # + + + # + + +                
                    + + # # # + + + # + + + +              
                  + + + +   + + + + # + + + + +            
                + + + + + + + + + + # + + + + + +          
              + + + # # # # # # # # # + + + + + + +        
            + + + + +               + + + + + + + + +      
'''
