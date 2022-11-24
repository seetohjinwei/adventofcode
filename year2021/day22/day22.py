from dataclasses import dataclass
from math import floor
import numpy as np
import re

with open("AoC 2021/day22/s.in") as f:
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

@dataclass
class Cube:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

def intersection(cube1: Cube, cube2: Cube):
    has_intersection = False
    cube_i = Cube(cube1.x1, cube1.x2, cube1.y1, cube1.y2, cube1.z1, cube1.z2)
    if cube2.x1 >= cube1.x1 and cube2.x1 <= cube1.x2:
        has_intersection = True
        cube_i.x1 = cube2.x1
    elif cube2.x2 >= cube1.x1 and cube2.x2 <= cube1.x2:
        has_intersection = True
        cube_i.x2 = cube2.x2
    elif cube2.y1 >= cube1.y1 and cube2.y1 <= cube1.y2:
        has_intersection = True
        cube_i.y1 = cube2.y1
    elif cube2.y2 >= cube1.y1 and cube2.y2 <= cube1.y2:
        has_intersection = True
        cube_i.y2 = cube2.y2
    elif cube2.z1 >= cube1.z1 and cube2.z1 <= cube1.z2:
        has_intersection = True
        cube_i.z1 = cube2.z1
    elif cube2.z2 >= cube1.z1 and cube2.z2 <= cube1.z2:
        has_intersection = True
        cube_i.z2 = cube2.z2
    return (has_intersection, cube_i)

def part2(data):
    cubes = []
    data = re.findall(r'(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', data)
    for instruction, x1, x2, y1, y2, z1, z2 in data:
        cube2 = Cube(x1, x2, y1, y2, z1, z2)
        for cube1 in cubes:
            has_intersection, cube_i = intersection(cube1, cube2)
            if has_intersection:
                if instruction == "on":
                    pass
                else:
                    cubes.remove(cube1)
                    cubes.append(Cube(cube1.x1, cube1.x2, cube1.y1, cube1.y2, cube1.z1, cube_i.z1))
                    cubes.append(Cube(cube1.x1, cube1.x2, cube1.y1, cube_i.y1, cube1.z1, cube_i.z1))
                    cubes.append(Cube(cube1.x1, cube_i.x1, cube1.y1, cube_i.y1, cube1.z1, cube_i.z1))
                    pass
                break
        else:
            if instruction == "on":
                cubes.append(cube2)
    print(len(cubes))

print("Part 2:", part2(data))
