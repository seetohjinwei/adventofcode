from math import floor
import numpy as np
import re

with open("AoC 2021/day22/a.in") as f:
    data = f.read()

def part1(data):
    cubes = np.zeros([101, 101, 101], dtype=bool)
    data = re.findall(r'(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', data)
    for instruction, x1, x2, y1, y2, z1, z2 in data:
        x1 = max(0, int(x1) + 50)
        x2 = min(101, int(x2) + 50 + 1)
        y1 = max(0, int(y1) + 50)
        y2 = min(101, int(y2) + 50 + 1)
        z1 = max(0, int(z1) + 50)
        z2 = min(101, int(z2) + 50 + 1)
        if instruction == "on":
            cubes[x1:x2, y1:y2, z1:z2] = 1
        else:
            cubes[x1:x2, y1:y2, z1:z2] = 0
    return floor(cubes.sum())

print("Part 1:", part1(data))

def part2(data):
    min_x = float("inf")
    max_x = -float("inf")
    min_y = float("inf")
    max_y = -float("inf")
    min_z = float("inf")
    max_z = -float("inf")
    digits = re.findall(r'x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', data)
    for line in digits:
        x1, x2, y1, y2, z1, z2 = map(int, line)
        min_x = min(x1, min_x)
        max_x = max(x2, max_x)
        min_y = min(y1, min_y)
        max_y = max(y2, max_y)
        min_z = min(z1, min_z)
        max_z = max(z2, max_z)
    cubes = np.zeros([max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1], dtype=bool)
    # I just need to get 6.35 PiB of RAM to get this thing to work

print("Part 2:", part2(data))
