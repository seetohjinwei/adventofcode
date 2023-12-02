from functools import reduce


with open("day02.in") as f:
    data = f.read().strip()


def get_part1(data: str) -> int:
    RED = 12
    GREEN = 13
    BLUE = 14

    result = 0

    for line in data.split("\n"):
        game, data = line.split(": ", 1)
        game = game[len("Game "):]

        impossible = False

        for move in data.split("; "):
            counts = {
                "red": RED,
                "green": GREEN,
                "blue": BLUE,
            }
            for cube in move.split(", "):
                count, colour = cube.split(" ")
                counts[colour] -= int(count)
                if counts[colour] < 0:
                    impossible = True
                    break

            if impossible:
                break

        if not impossible:
            result += int(game)

    return result


def get_part2(data: str) -> int:
    result = 0

    for line in data.split("\n"):
        game, data = line.split(": ", 1)
        game = game[len("Game "):]

        powers = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for move in data.split("; "):
            for cube in move.split(", "):
                count, colour = cube.split(" ")
                powers[colour] = max(powers[colour], int(count))

        result += reduce(lambda acc, x: acc * x, powers.values())

    return result


part1 = get_part1(data)
part2 = get_part2(data)

print(f"part1: {part1}")
print(f"part2: {part2}")
