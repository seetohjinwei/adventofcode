from collections import deque
from math import prod


with open("day11.in") as f:
    data = f.read().strip()

'''
Iterate each monke
    Iterate each item
        1. Execute operation on item's worry
        2. Item's worry // 3
        3. Test & throw to respective monke
'''

class Monke:
    def __init__(self, s):
        self.items = deque()
        _, items, op, test, a, b = s.split("\n")
        for x in items[18:].split(", "):
            self.items.append(int(x))
        self.op = lambda old: eval(op[19:])
        self.tester = int(test[21:])
        self.test = lambda val: val % int(test[21:]) == 0
        self.true = int(a[29:])
        self.false = int(b[30:])
        self.inspected = 0

    def __repr__(self):
        return f"{self.items} true: {self.true} false: {self.false}"

monkes1 = [Monke(s) for s in data.split("\n\n")]
monkes2 = [Monke(s) for s in data.split("\n\n")]
mod_ = prod(m.tester for m in monkes1)

def do(monkes, rounds, remove_worry):
    for _ in range(rounds):
        for m in monkes:
            iters = len(m.items)
            while iters > 0:
                iters -= 1
                m.inspected += 1
                x = m.items.popleft()
                x = m.op(x)
                if remove_worry:
                    x //= 3
                x %= mod_
                if m.test(x):
                    new_monke = m.true
                else:
                    new_monke = m.false
                monkes[new_monke].items.append(x)

do(monkes1, 20, True)
inspections = sorted(m.inspected for m in monkes1)
part1 = inspections[-2] * inspections[-1]

do(monkes2, 10000, False)
inspections = sorted(m.inspected for m in monkes2)
part2 = inspections[-2] * inspections[-1]

print(f"part1: {part1}")
print(f"part2: {part2}")
