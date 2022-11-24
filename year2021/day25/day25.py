with open("AoC 2021/day25/a.in") as f:
    grid = [[x for x in row] for row in f.read().split("\n")]

def east_check(grid, r, c):
    if c == len(grid[0]) - 1:
        # last column
        return (grid[r][0] == '.', r, 0)
    else:
        return (grid[r][c+1] == '.', r, c+1)

def south_check(grid, r, c):
    if r == len(grid) - 1:
        # last row
        return (grid[0][c] == '.', 0, c)
    else:
        return (grid[r+1][c] == '.', r+1, c)

def solve(grid):
    steps = 0
    solving = True
    prev = grid
    while solving:
        next = [['' for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # east
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '>':
                    move, new_r, new_c = east_check(grid, r, c)
                    if move:
                        next[r][c] = '.'
                        next[new_r][new_c] = '>'
                    else:
                        next[r][c] = grid[r][c]
                elif next[r][c] == '':
                    next[r][c] = grid[r][c]
        grid = next
        next = [['' for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # south
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'v':
                    move, new_r, new_c = south_check(grid, r, c)
                    if move:
                        next[r][c] = '.'
                        next[new_r][new_c] = 'v'
                    else:
                        next[r][c] = grid[r][c]
                elif next[r][c] == '':
                    next[r][c] = grid[r][c]
        grid = next
        steps += 1
        if grid == prev:
            solving = False
        prev = grid
    return steps

print("Part 1:", solve(grid))
