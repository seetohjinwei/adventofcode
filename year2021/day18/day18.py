import re

with open("AoC 2021/day18/s.in") as f:
    lines = list(map(lambda line: line.strip("\n"), f.readlines()))

def eval_pair(pair):
    m = re.match(r'^\[(.+),(.+)\]$', pair)
    return (m.group(1), m.group(2))

def help_explode(string):
    opened = 0
    found = 0
    start = None
    end = None
    for i, c in enumerate(string):
        if c == '[':
            opened += 1
        elif c == ']':
            opened -= 1
        if opened == 5 and not found:
            found = i
        if opened == 4 and found:
            start = found
            end = i
            # print(string[found:i+1])
            break
        i += 1
    if not found:
        return (False, string)
    nested = string[found:i+1]
    first, second = re.findall(r'\d+', nested)
    if string[found-1] == ',':
        # literal, pair
        num = ""
        for i in range(found-2, 0, -1):
            c = string[i]
            if c in "1234567890":
                num = c + num
            else:
                break
        res = str(int(num) + int(first))
    else:
        # pair, literal
        num = ""
        for i in range(i+2, len(string)):
            c = string[i]
            if c in "1234567890":
                num = num + c
            else:
                break
        res = str(int(second) + int(num))
    print(res)

def explode(string):
    m = re.search(r'(\[[^\[\]]*\[[^\[\]]*\][^\[\]]*\])(?=.*\].*\].*\])', string)
    # m = re.search(r'(\[[^\[\]]*\])(?=.*\].*\].*\].*\])', string)
    if m:
        target = m.group(0)
        print(target)
        first, second, third = re.findall(r'\d+', target)
        # print(first, second, third)
        if re.search(r'^\[\[', target):
            # pair, literal
            new_val = '[0,' + str(int(second) + int(third)) + ']'
            print(new_val)
            pass
        else:
            # literal, pair
            new_val = '[' + str(int(first) + int(second)) + ',0]'
            print(new_val)
            pass
        return True
    else:
        return string 

def reduce(string):
    # haven't implement
    return string

current = lines[0]
# for i in range(1, len(lines)):
#     line = lines[i]
#     current = '[' + current + ',' + line + ']'
#     current = reduce(current)

for line in lines:
    # print(explode(line))
    # explode(line)
    print(help_explode(line))
