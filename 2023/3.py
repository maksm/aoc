day = 3

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# lines = test.splitlines()[1:]

NEIGH_2D_DIAG = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

numbers = {}
nondots = {}
num_key = None
num = None
num_set = set()
for j, line in enumerate(lines):
    for i, ch in enumerate(line):
        if ch.isnumeric():
            if not num:
                num_key = (i, j)
                num_set.add((i, j))
                num = ch
            else:
                num_set.add((i, j))
                num += ch
        else:
            if num:
                numbers[num_key] = {'num': num, 'set': num_set}
                num_set = set()
                num = None
            if ch != ".":
                nondots[(i, j)] = ch
    if num:
        numbers[num_key] = {'num': num, 'set': num_set}
        num = None
        num_set = set()
if num:
    numbers[num_key] = {'num': num, 'set': num_set}

def check_number_neigh(x, y):
    neighs = set()
    for j in range(len(numbers[(x, y)]['num'])):
        for dx, dy in NEIGH_2D_DIAG:
            if (x + j + dx, y + dy) in nondots:
                neighs.add((x + j + dx, y + dy))
    return neighs

s = 0
number_neighs = {}
for (x, y), num_dict in numbers.items():
    neighs = check_number_neigh(x, y)
    if len(neighs) > 0:
        s += int(num_dict['num'])
        number_neighs[(x, y)] = neighs
print(s) 

# part 2
gears_neighs = {}
for (x, y), neighs in number_neighs.items():
    for (x1, y1) in neighs:
        if nondots[(x1, y1)] == '*':
            if not (x1, y1) in gears_neighs:
                gears_neighs[(x1, y1)] = set()
            gears_neighs[(x1, y1)].add((x, y))

s = 0
for k, v in gears_neighs.items():
    if len(v) != 2:
        continue
    m = 1
    for (x, y) in v:
        m *= int(numbers[(x, y)]['num'])
    s += m
print(s)

