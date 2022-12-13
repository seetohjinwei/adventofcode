'''
part1: #1234 22:33
part2: #1270 31:23

In part 1, I didn't read the prompt properly and didn't realise that I needed a 3-state boolean.
In part 2, I wasn't familiar enough with python's sorting comparator and spent couple of minutes googling.

`eval` came in clutch again as a time-saver for parsing.
'''
from enum import Enum, auto
from functools import cmp_to_key


with open("day13.in") as f:
    data = f.read().strip()

class Bool(Enum):
    TRUE = auto()
    FALSE = auto()
    IDK = auto()

def isRight(x, y):
    x_list = isinstance(x, list)
    y_list = isinstance(y, list)

    # both integers
    if not x_list and not y_list:
        if x < y:
            return Bool.TRUE
        elif x > y:
            return Bool.FALSE
        return Bool.IDK

    # convert integer to list
    if not x_list:
        x = [x]
    if not y_list:
        y = [y]

    for a, b in zip(x, y):
        _bool = isRight(a, b)
        if _bool != Bool.IDK:
            return _bool

    # length checks
    if len(x) < len(y):
        return Bool.TRUE
    elif len(x) > len(y):
        return Bool.FALSE
    return Bool.IDK

data1 = [x.split("\n") for x in data.split("\n\n")]
part1 = 0

for i, (x, y) in enumerate(data1):
    x = eval(x)
    y = eval(y)
    if isRight(x, y) == Bool.TRUE:
        part1 += i + 1

def comparator(x, y):
    if isRight(x, y) == Bool.TRUE:
        return -1
    elif isRight(x, y) == Bool.FALSE:
        return 1
    return 0

first = [[2]]
second = [[6]]

data2 = [eval(y) for y in data.split("\n") if y != ""]
data2.append(first)
data2.append(second)
data2.sort(key=cmp_to_key(comparator))

part2 = (data2.index(first) + 1) * (data2.index(second) + 1)

print(f"part1: {part1}")
print(f"part2: {part2}")
