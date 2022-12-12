'''
part1: #998 19:53
part2: #952 23:22
'''
from collections import deque


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def add(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))

with open("day12.in") as f:
    data = f.read().strip()

data = [[c for c in r] for r in data.split("\n")]
m = len(data)
n = len(data[0])

def in_range(t):
    r, c = t
    return r >= 0 and r < m and c >= 0 and c < n

def valid_climb(x, y):
    if x == "S":
        return True
    if y == "E":
        y = "z"

    x = ord(x)
    y = ord(y)

    return x >= y - 1

queue1 = deque()
steps1 = [[float("inf") if data[i][j] != "S" else 0 for j in range(n)] for i in range(m)]
queue2 = deque()
steps2 = [[float("inf") if data[i][j] != "S" else 0 for j in range(n)] for i in range(m)]

for i, r in enumerate(data):
    for j, k in enumerate(r):
        if k == "S":
            steps1[i][j] = 0
            queue1.append((i, j))
            steps2[i][j] = 0
            queue2.append((i, j))
        if k == "a":
            steps2[i][j] = 0
            queue2.append((i, j))

def bfs(steps, queue):
    while queue:
        count = len(queue)
        while count > 0:
            count -= 1

            r, c = queue.popleft()
            new_step = steps[r][c] + 1
            for d in DIRS:
                r2, c2 = add((r, c), d)
                if in_range((r2, c2)) and valid_climb(data[r][c], data[r2][c2]):
                    if new_step < steps[r2][c2]:
                        steps[r2][c2] = new_step
                        queue.append((r2, c2))

bfs(steps1, queue1)
bfs(steps2, queue2)

def crunch():
    for i, r in enumerate(data):
        for j, k in enumerate(r):
            if k == "E":
                return steps1[i][j], steps2[i][j]

part1, part2 = crunch()
print(f"part1: {part1}")
print(f"part2: {part2}")
