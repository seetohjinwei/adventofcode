with open("Aoc 2021/day20/a.in") as f:
    data = f.readlines()
    algorithm = data[0]
    original_image = data[2:]

def get_value(image, r, c, flip):
    if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
        # only true for a.in (background flipping)
        return '0' if flip else '1'
        # return '0' (for s.in)
    elif image[r][c] == '#':
        return '1'
    else:
        return '0'

def get_grid(image, r, c, flip):
    result = []
    for x in range(r - 1, r + 2):
        for y in range(c - 1, c + 2):
            result.append(get_value(image, x, y, flip))
    return int(''.join(result), 2)

def driver(image, flip):
    rows = len(image) + 2
    cols = len(image[0]) + 2
    result = []
    for r in range(rows):
        R = []
        for c in range(cols):
            index = get_grid(image, r - 1, c - 1, flip)
            R.append(algorithm[index])
        result.append(R)
    return result

def count_lit(image):
    return sum(1 for row in image for x in row if x == '#')

def solve(n):
    image = list(list(c for c in line.strip()) for line in original_image)
    for i in range(n):
        flip = i % 2 == 0
        image = driver(image, flip)
    print(count_lit(image))

solve(2)
solve(50)
