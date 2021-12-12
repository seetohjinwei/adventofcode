# part 2

data = list(map(int, open("day01/a.in").read().split()))
prev_window = data[0] + data[1] + data[2]

result = 0

for i, n in enumerate(data):
    if i < 3:
        continue
    new_window = prev_window - data[i - 3] + n
    if new_window > prev_window:
        result += 1
    prev_window = new_window

print(result)
