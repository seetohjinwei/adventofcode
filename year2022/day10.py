with open("day10.in") as f:
    data = f.read().strip()

part1 = 0
X = 1
cycle = 1

part2 = [" " for _ in range(40 * 6)]

def do(part1, part2, cycle):
    if cycle % 40 == 20:
        part1 += cycle * X

    pos = (cycle - 1) % 40 + 1
    if X - 1 <= pos - 1 and pos - 1 <= X + 1:
        part2[cycle - 1] = u"\u2588"

    return part1

do(part1, part2, cycle)

for line in data.split("\n"):
    if line == "noop":
        cycle += 1
        part1 = do(part1, part2, cycle)
    else:
        _, val = line.split(" ")
        cycle += 2

        # before
        part1 = do(part1, part2, cycle - 1)
        X += int(val)
        # after
        part1 = do(part1, part2, cycle)

if cycle % 40 == 20:
    part1 += cycle * X

print(f"part1: {part1}")
print("part2:")
print("\033[1;32;48m", end="")
for i in range(0, len(part2), 40):
    print("".join(part2[i:i+40]))

'''
part1: 11820
part2:
████ ███    ██ ███  ███  █  █  ██  █  █
█    █  █    █ █  █ █  █ █ █  █  █ █  █
███  █  █    █ ███  █  █ ██   █  █ ████
█    ███     █ █  █ ███  █ █  ████ █  █
█    █    █  █ █  █ █ █  █ █  █  █ █  █
████ █     ██  ███  █  █ █  █ █  █ █  █
'''
