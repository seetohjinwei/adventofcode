from functools import cache

with open("AoC 2021/day21/a.in") as f:
    data = f.readlines()
    pos1 = int(data[0][-2])
    pos2 = int(data[1][-1])

def calc(die):
    return ((die) % 100 + 1) + ((die + 1) % 100 + 1) + ((die + 2) % 100 + 1)

def part1(pos1, pos2):
    score1 = 0
    score2 = 0
    die = 0
    game = True
    player1 = True
    while game:
        if player1:
            pos1 = (pos1 + calc(die) - 1) % 10 + 1
            score1 += pos1
        else:
            pos2 = (pos2 + calc(die) - 1) % 10 + 1
            score2 += pos2
        if score1 >= 1000 or score2 >= 1000:
            game = False
        die += 3
        player1 = not player1
    return min(score1, score2) * die

print("Part 1:", part1(pos1, pos2))

@cache
def recurse(turn1, turn2, pos1, pos2, score1, score2):
    if score1 >= 21:
        return (1, 0)
    elif score2 >= 21:
        return (0, 1)
    if turn1 > 0:
        a_pos = (pos1 + 1 - 1) % 10 + 1
        b_pos = (pos1 + 2 - 1) % 10 + 1
        c_pos = (pos1 + 3 - 1) % 10 + 1
        a_score = score1
        b_score = score1
        c_score = score1
        if turn1 - 1 == 0:
            a_score = score1 + a_pos
            b_score = score1 + b_pos
            c_score = score1 + c_pos
            turn2 = 3
        a = recurse(turn1 - 1, turn2, a_pos, pos2, a_score, score2)
        b = recurse(turn1 - 1, turn2, b_pos, pos2, b_score, score2)
        c = recurse(turn1 - 1, turn2, c_pos, pos2, c_score, score2)
        return (a[0] + b[0] + c[0], a[1] + b[1] + c[1])
    else:
        a_pos = (pos2 + 1 - 1) % 10 + 1
        b_pos = (pos2 + 2 - 1) % 10 + 1
        c_pos = (pos2 + 3 - 1) % 10 + 1
        a_score = score2
        b_score = score2
        c_score = score2
        if turn2 - 1 == 0:
            a_score = score2 + a_pos
            b_score = score2 + b_pos
            c_score = score2 + c_pos
            turn1 = 3
        b = recurse(turn1, turn2 - 1, pos1, b_pos, score1, b_score)
        a = recurse(turn1, turn2 - 1, pos1, a_pos, score1, a_score)
        c = recurse(turn1, turn2 - 1, pos1, c_pos, score1, c_score)
        return (a[0] + b[0] + c[0], a[1] + b[1] + c[1])

print("Part 2:", max(recurse(3, 0, pos1, pos2, 0, 0)))
# runs in 0.153 because @cache
