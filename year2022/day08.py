'''
part1: #543 08:06
part2: #459 16:20
'''

with open("day08.in") as f:
    data = f.read().strip()
    trees = [[int(t) for t in row] for row in data.split("\n")]
    m = len(trees)
    n = len(trees[0])

visible = [[False for _ in range(n)] for _ in range(m)]

# top-down
for c in range(n):
    top = -1
    bot = -1
    for r in range(m):
        x = trees[r][c]
        y = trees[m - r - 1][c]
        if x > top:
            visible[r][c] = True
        if y > bot:
            visible[m - r - 1][c] = True
        top = max(top, x)
        bot = max(bot, y)

# left-right
for r in range(m):
    left = -1
    right = -1
    for c in range(n):
        x = trees[r][c]
        y = trees[r][n - c - 1]
        if x > left:
            visible[r][c] = True
        if y > right:
            visible[r][n - c - 1] = True
        left = max(left, x)
        right = max(right, y)

part1 = sum(sum(row) for row in visible)

visible = [[1 for _ in range(n)] for _ in range(m)]

for r in range(m):
    for c in range(n):
        height = trees[r][c]

        count = 0
        x = r - 1
        while x >= 0:
            count += 1
            if trees[x][c] >= height:
                break
            x -= 1
        val = count

        count = 0
        x = r + 1
        while x < m:
            count += 1
            if trees[x][c] >= height:
                break
            x += 1
        val *= count

        count = 0
        y = c - 1
        while y >= 0:
            count += 1
            if trees[r][y] >= height:
                break
            y -= 1
        val *= count

        count = 0
        y = c + 1
        while y < n:
            count += 1
            if trees[r][y] >= height:
                break
            y += 1
        val *= count

        visible[r][c] = val

part2 = max(max(row) for row in visible)

print(f"part1: {part1}")
print(f"part2: {part2}")
