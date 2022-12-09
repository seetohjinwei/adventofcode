with open("day09.in") as f:
    data = f.read().strip()

DIRS = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}

visited = set()

H = (0, 0)
T = (0, 0)

visited.add(T)

for row in data.split("\n"):
    d, amt = row.split(" ")
    amt = int(amt)
    while amt > 0:
        x, y = DIRS[d]
        H = (H[0] + x, H[1] + y)

        x_delta = H[0] - T[0]
        y_delta = H[1] - T[1]

        amt -= 1

        # are touching, don't do anything
        if not(
            (x_delta == 0 and abs(y_delta) >= 2)
            or (y_delta == 0 and abs(x_delta) >= 2)
            or (abs(x_delta) + abs(y_delta) >= 3)
        ):
            continue

        if y_delta < 0:
            T = (T[0], T[1] - 1)
        elif y_delta > 0:
            T = (T[0], T[1] + 1)
        if x_delta < 0:
            T = (T[0] - 1, T[1])
        elif x_delta > 0:
            T = (T[0] + 1, T[1])
        visited.add(T)

part1 = len(visited)

visited = set()

TS = [(0, 0) for _ in range(10)]

visited.add(TS[-1])

for row in data.split("\n"):
    d, amt = row.split(" ")
    amt = int(amt)
    while amt > 0:
        x, y = DIRS[d]
        TS[0] = (TS[0][0] + x, TS[0][1] + y)

        amt -= 1

        for i in range(1, 10):
            T = TS[i]
            x_delta = TS[i - 1][0] - T[0]
            y_delta = TS[i - 1][1] - T[1]

            # are touching, don't do anything
            if not(
                (x_delta == 0 and abs(y_delta) >= 2)
                or (y_delta == 0 and abs(x_delta) >= 2)
                or (abs(x_delta) + abs(y_delta) >= 3)
            ):
                continue

            if y_delta < 0:
                T = (T[0], T[1] - 1)
            elif y_delta > 0:
                T = (T[0], T[1] + 1)
            if x_delta < 0:
                T = (T[0] - 1, T[1])
            elif x_delta > 0:
                T = (T[0] + 1, T[1])

            TS[i] = T

        visited.add(TS[-1])

part2 = len(visited)

print(f"part1: {part1}")
print(f"part2: {part2}")
