data = open("day3.in").read().split("\n")

def part1():
    size = len(data[0])
    ones = [sum(1 for x in data if x[i] == '0') for i in range(size)]
    zero = [len(data) - x for x in ones]
    g = ['0' if o > z else '1' for o, z in zip(ones, zero)]
    p = ['0' if x == '1' else '1' for x in g]
    gamma = int(''.join(g), 2)
    power = int(''.join(p), 2)
    print(gamma * power)

def part2():
    d = data.copy()
    size = len(d[0])
    for i in range(size):
        count_total = len(d)
        if count_total == 1:
            break
        count_zero = sum(1 for x in d if x[i] == '0')
        to_keep = '0' if count_zero > count_total / 2 else '1'
        d = list(filter(lambda x: x[i] == to_keep, d))
    oxygen = int(''.join(d), 2)
    
    d = data.copy()
    for i in range(size):
        count_total = len(d)
        if count_total == 1:
            break
        count_zero = sum(1 for x in d if x[i] == '0')
        to_keep = '0' if count_zero <= count_total / 2 else '1'
        d = list(filter(lambda x: x[i] == to_keep, d))
    co2 = int(''.join(d), 2)
    print(oxygen * co2)

part1()
part2()
