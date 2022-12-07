with open("day07.in") as f:
    data = f.read().strip()

folders = {}
current = []
folders["/"] = 0

for line in data.split("\n"):
    v = line.split(" ")
    if v[0] == "$":
        if v[1] == "cd":
            if v[2] == "..":
                current.pop(-1)
            else:
                current.append(v[2])
    elif v[0] == "dir":
        folder = "-".join(current) + "-" + v[1]
        folders[folder] = 0
    else:
        size = int(v[0])
        acc = ""
        for i, f in enumerate(current):
            if i == 0:
                acc = f
            else:
                acc += "-" + f
            folders[acc] += size

part1 = 0
required = folders["/"] - 40000000
part2 = float("inf")
for size in folders.values():
    if size <= 100000:
        part1 += size
    if size >= required:
        part2 = min(size, part2)

print(f"part1: {part1}")
print(f"part2: {part2}")
