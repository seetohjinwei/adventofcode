import re


with open("day01.in") as f:
    data = f.read().strip()


def get_part1(data: str) -> int:
    pattern = re.compile(r"(\d)")

    result = 0
    for line in data.split("\n"):
        digits = pattern.findall(line)
        result += int(digits[0] + digits[-1])

    return result


def get_part2(data: str):
    numbers = [str(i) for i in range(1, 9+1)] + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # regex greedily matches, so we can't do that :/ (or at least I couldn't find a way to)
    # pattern = re.compile(rf"(\d|{'|'.join(numbers)})")

    def get_digit(num: str) -> int:
        index = numbers.index(num)
        return (index % 9) + 1

    # brute force is still instant :)
    result = 0
    for line in data.split("\n"):
        results = []

        for num in numbers:
            i = 0
            while i < len(line):
                index = line.find(num, i)
                if index < 0:
                    break
                i = index + 1
                results.append((index, num))

        results.sort()
        result += get_digit(results[0][1]) * 10 + get_digit(results[-1][1])

        # digits = pattern.findall(line)
        # print(line, digits, get_digit(digits[0]) * 10 + get_digit(digits[-1]))
        # result += get_digit(digits[0]) * 10 + get_digit(digits[-1])

    return result


part1 = get_part1(data)
part2 = get_part2(data)

print(f"part1: {part1}")
print(f"part2: {part2}")
