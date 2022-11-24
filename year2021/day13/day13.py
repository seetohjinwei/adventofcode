import numpy as np
import re

max_x = 0
max_y = 0
x_points = []
y_points = []
instructions = []

# parsing input
with open("AoC 2021/day13/a.in") as f:
    lines = f.readlines()
    reading_points = True
    for line in lines:
        line = line.strip()
        if line == "":
            reading_points = False
        elif reading_points:
            x, y = map(int, line.split(","))
            x_points.append(x)
            y_points.append(y)
            max_x = max(x + 1, max_x)
            max_y = max(y + 1, max_y)
        else:
            a, b = re.findall(r"x|y|\d+", line)
            instructions.append((a, int(b)))

# initialising array
arr = np.zeros((max_y, max_x), dtype=bool)
arr[y_points, x_points] = 1

for i, (direction, si) in enumerate(instructions):
    if direction == "x":
        # left | right
        arr = arr[:, :si] | arr[:, max_x : si : -1]
    else:
        # top | bot
        arr = arr[:si, :] | arr[max_y : si : -1, :]
    if i == 0:
        print("Part 1:", arr.sum())

print("Part 2:")
print(np.array2string(arr, separator="", formatter={"bool": {0: " ", 1: "█"}.get}))
