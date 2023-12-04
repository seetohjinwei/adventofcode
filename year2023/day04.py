import re


with open("day04.in") as f:
    data = f.read().strip()


def get_part1(data: str) -> int:
    def parse(numbers: str) -> set[int]:
        pattern = re.compile(r"\d+")
        return set(int(n) for n in pattern.findall(numbers))

    result = 0

    for line in data.split("\n"):
        _, numbers = line.split(": ", 1)
        winning, mine = numbers.split(" | ", 1)
        winning = parse(winning)
        mine = parse(mine)
        matches = winning.intersection(mine)
        if matches:
            result += 1 << (len(matches) - 1)

    return result


def get_part2(data: str) -> int:
    def parse(numbers: str) -> set[int]:
        pattern = re.compile(r"\d+")
        return set(int(n) for n in pattern.findall(numbers))

    copies = [1 for _ in range(data.count("\n") + 1)]

    for i, line in enumerate(data.split("\n")):
        _, numbers = line.split(": ", 1)
        winning, mine = numbers.split(" | ", 1)
        winning = parse(winning)
        mine = parse(mine)
        matches = winning.intersection(mine)
        for j in range(i + 1, i + 1 + len(matches)):
            copies[j] += copies[i]

    return sum(copies)


part1 = get_part1(data)
part2 = get_part2(data)

print(f"part1: {part1}")
print(f"part2: {part2}")
