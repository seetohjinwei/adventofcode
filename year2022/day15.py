from re import findall


with open("day15.in") as f:
    data = f.read().strip()

data1 = [[int(x[1]) for x in findall(r"(x|y)=(-?\d+)", line)] for line in data.split("\n")]
data2 = [[int(x[1]) for x in findall(r"(x|y)=(-?\d+)", line)] for line in data.split("\n")]

def get_dist(sensor):
    x1, y1, x2, y2 = sensor
    return abs(x1 - x2) + abs(y1 - y2)

def get_bounds(sensor, y):
    r = get_dist(sensor)
    x1, y1, _, _ = sensor

    abs_ = abs(y - y1)
    s = abs_ - r + x1
    e = r - abs_ + x1
    if s <= e:
        return [s, e]
    return None

def get_intervals(data, y):
    intervals = []

    for sensor in data:
        interval = get_bounds(sensor, y)
        if interval is not None:
            intervals.append(interval)

    return intervals

def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    result = []
    x = intervals[0]

    for y in intervals[1:]:
        if x[1] + 1 >= y[0]:
            # merge them
            x[1] = max(x[1], y[1])
        else:
            result.append(x)
            x = y
    result.append(x)

    return result

def count_intervals(data, y, intervals):
    count = sum(x[1] - x[0] + 1 for x in intervals)

    exclude = set()

    for sensor in data:
        _, _, x1, y1 = sensor
        if y1 == y:
            exclude.add(x1)

    return count - len(exclude)

def crunch1(data, y):
    x = get_intervals(data, y)
    x = merge_intervals(x)
    return count_intervals(data, y, x)

def tuning_frequency(x, y):
    return x * 4000000 + y

'''
brute force, takes 36 seconds on my machine .-.
'''
def crunch2(data, max_):
    for y in range(0, max_ + 1):
        x = merge_intervals(get_intervals(data, y))
        if len(x) == 2:
            return tuning_frequency(x[1][0] - 1, y)

part1 = crunch1(data1, 2000000)
part2 = crunch2(data2, 4000000)

print(f"part1: {part1}")
print(f"part2: {part2}")
