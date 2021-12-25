import re

with open("AoC 2021/day24/a.in") as f:
    instructions = f.read()

def is_number(x):
    return re.match(r'^-?\d+$', x)

def run(number, instructions):
    vars = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    index = 0
    for line in instructions.split("\n"):
        params = line.split(" ")
        command = params[0]
        var = params[1]
        if command == 'inp':
            vars[var] = int(number[index])
            index += 1
        else:
            second = params[2]
            if is_number(second):
                second = int(second)
            else:
                second = vars[second]
            if command == 'add':
                vars[var] += second
            elif command == 'mul':
                vars[var] *= second
            elif command == 'div':
                vars[var] = vars[var] // second
            elif command == 'mod':
                vars[var] = vars[var] % second
            elif command == 'eql':
                vars[var] = 1 if vars[var] == second else 0
            else:
                raise ValueError
    return vars

# sample tests
assert run("1", '''inp x
mul x -1''')['x'] == -1
assert run("26", '''inp z
inp x
mul z 3
eql z x''')['z'] == 1
assert run("9", '''inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2''') == {'w': 1, 'x': 0, 'y': 0, 'z': 1}

def part1(instructions):
    for n in range(99999999999999, 0, -1):
        n = str(n)
        if re.search(r'0', n):
            pass
            # skip
        else:
            if n[-3] == '9' and n[-2] == '9' and n[-1] == '9':
                print(n)
            vars = run(n, instructions)
            if vars['z'] == 0:
                print(n)
                return n
                break

print("Part 1:", part1(instructions))

