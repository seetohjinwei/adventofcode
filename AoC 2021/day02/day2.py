def helper(x):
    a, b = x.split()
    return (a, int(b))

data = list(map(helper, open("day2/a.in").read().split("\n")))

def part1():
    horizontal = 0
    depth = 0

    for instruction, amount in data:
        if instruction == "forward":
            horizontal += amount
        elif instruction == "down":
            depth += amount
        elif instruction == "up":
            depth -= amount

    print(horizontal * depth)


def part2():
    aim = 0
    horizontal = 0
    depth = 0

    for instruction, amount in data:
        if instruction == "forward":
            horizontal += amount
            depth += aim * amount
        elif instruction == "down":
            aim += amount
        elif instruction == "up":
            aim -= amount

    print(horizontal * depth)

part1()
part2()
