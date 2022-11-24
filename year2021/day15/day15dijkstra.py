# wrote in Dijkstra's Algorithm (after my Java solution)
import heapq

with open("AoC 2021/day15/a.in") as f:
    lines = f.readlines()

data = [[int(d) for d in line.strip()] for line in lines]
rows = len(data)
cols = len(data[0])

# Part 1
nrows = rows
ncols = cols
L = [[float("inf") for _ in range(cols)] for _ in range(rows)]
L[0][0] = 0
vertices = {(0, 0)}
fringe = [(0, 0, 0)]
v = (0, 0)

while (rows - 1, cols - 1) not in vertices:
    r = v[0]
    c = v[1]
    adjacent = set()
    if r + 1 < rows:
        adjacent.add((r + 1, c))
    if r - 1 >= 0:
        adjacent.add((r - 1, c))
    if c + 1 < cols:
        adjacent.add((r, c + 1))
    if c - 1 >= 0:
        adjacent.add((r, c - 1))
    to_consider = adjacent.difference(vertices)
    for u in to_consider:
        if L[v[0]][v[1]] + data[u[0]][u[1]] < L[u[0]][u[1]]:
            L[u[0]][u[1]] = L[v[0]][v[1]] + data[u[0]][u[1]]
        heapq.heappush(fringe, (L[u[0]][u[1]], u[0], u[1]))
    while v in vertices:
        d, r, c = heapq.heappop(fringe)
        v = (r, c)
    vertices.add(v)

print("Part 1:", L[rows - 1][cols - 1])

# Part 2
nrows = rows * 5
ncols = cols * 5
L = [[float("inf") for _ in range(ncols)] for _ in range(nrows)]
L[0][0] = 0
vertices = {(0, 0)}
fringe = [(0, 0, 0)]
v = (0, 0)

while (nrows - 1, ncols - 1) not in vertices:
    r = v[0]
    c = v[1]
    adjacent = set()
    if r + 1 < nrows:
        adjacent.add((r + 1, c))
    if r - 1 >= 0:
        adjacent.add((r - 1, c))
    if c + 1 < ncols:
        adjacent.add((r, c + 1))
    if c - 1 >= 0:
        adjacent.add((r, c - 1))
    to_consider = adjacent.difference(vertices)
    for u in to_consider:
        val = data[u[0] % rows][u[1] % cols]
        mod = u[0] // rows + u[1] // cols
        nval = (val + mod - 1) % 9 + 1
        if L[v[0]][v[1]] + nval < L[u[0]][u[1]]:
            L[u[0]][u[1]] = L[v[0]][v[1]] + nval
        heapq.heappush(fringe, (L[u[0]][u[1]], u[0], u[1]))
    while v in vertices:
        d, r, c = heapq.heappop(fringe)
        v = (r, c)
    vertices.add(v)

print("Part 2:", L[nrows - 1][ncols - 1])
