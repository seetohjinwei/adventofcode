import re

with open("AoC 2021/day17/a.in") as f:
    x_lower, x_upper, y_lower, y_upper = map(int, re.findall(r'-?\d+', f.read()))

def probe(x_velocity, y_velocity):
    x, y = 0, 0
    highest_y = 0
    while x >= 0 and x <= x_upper and y >= y_lower:
        x += x_velocity
        y += y_velocity
        x_velocity -= 1 if x_velocity > 0 else 0
        y_velocity -= 1
        highest_y = max(y, highest_y)
        if x >= x_lower and x <= x_upper and y >= y_lower and y <= y_upper:
            return (True, highest_y)
    return (False, 0)

highest_y = 0
total_success = 0
# using numbers that (should be) way above the answer
for x_velocity in range(1, 1000):
    for y_velocity in range(-1000, 1000):
        success, score = probe(x_velocity, y_velocity)
        if success:
            total_success += 1
            highest_y = max(score, highest_y)

print("Part 1:", highest_y)
print("Part 2:", total_success)
