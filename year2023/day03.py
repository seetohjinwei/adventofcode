import re


with open("day03.in") as f:
    data = f.read().strip()


def get_part1(data: str) -> int:
    class Object:
        def __init__(self, num: int, row: int, col_lo: int, col_hi: int):
            self.num = num
            self.row = row
            self.col_lo = col_lo
            self.col_hi = col_hi
            self.is_result = False

        def mark(self, row: int, col: int) -> None:
            if abs(row - self.row) <= 1 and (col >= self.col_lo - 1 and col <= self.col_hi + 1):
                self.is_result = True

    objects = []

    pattern = re.compile(r"\d+")
    for row, line in enumerate(data.split("\n")):
        for m in pattern.finditer(line):
            num = int(m.group(0))
            col_lo = m.start(0)
            col_hi = m.end(0) - 1
            obj = Object(num, row, col_lo, col_hi)
            objects.append(obj)

    pattern = re.compile(r"[^\d\.]")
    for row, line in enumerate(data.split("\n")):
        for m in pattern.finditer(line):
            for obj in objects:
                obj.mark(row, m.start(0))

    return sum(obj.num for obj in objects if obj.is_result)


def get_part2(data: str) -> int:
    class Object:
        def __init__(self, num: int, row: int, col_lo: int, col_hi: int):
            self.num = num
            self.row = row
            self.col_lo = col_lo
            self.col_hi = col_hi
            self.is_result = True

        def mark(self, row: int, col: int) -> bool:
            if abs(row - self.row) <= 1 and (col >= self.col_lo - 1 and col <= self.col_hi + 1):
                self.is_result = True
                return True
            return False

    objects = []

    pattern = re.compile(r"\d+")
    for row, line in enumerate(data.split("\n")):
        for m in pattern.finditer(line):
            num = int(m.group(0))
            col_lo = m.start(0)
            col_hi = m.end(0) - 1
            obj = Object(num, row, col_lo, col_hi)
            objects.append(obj)

    result = 0
    pattern = re.compile(r"\*")
    for row, line in enumerate(data.split("\n")):
        for m in pattern.finditer(line):
            found = []
            for obj in objects:
                if obj.mark(row, m.start(0)):
                    found.append(obj.num)
            if len(found) == 2:
                result += found[0] * found[1]

    return result


part1 = get_part1(data)
part2 = get_part2(data)

print(f"part1: {part1}")
print(f"part2: {part2}")
