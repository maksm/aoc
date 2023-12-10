day = 10

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()


test = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

# lines = test.splitlines()[1:]

MAP = {}
START = None
for j, line in enumerate(lines):
    for i, ch in enumerate(line):
        if ch == ".":
            continue
        if ch == "S":
            START = (i, j)
        MAP[(i, j)] = ch

PIPES = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((-1, 0), (0, 1)),
    "F": ((1, 0), (0, 1)),
}


def get_neighs(i0, j0, candidates):
    neighs = []
    for i, j in candidates:
        i1 = i0 + i
        j1 = j0 + j
        if (i1, j1) not in MAP:
            continue
        for dx, dy in PIPES[MAP[(i1, j1)]]:
            if (i1 + dx, j1 + dy) == (i0, j0):
                neighs.append((i1, j1))
    return neighs


start_n = get_neighs(*START, ((-1, 0), (1, 0), (0, -1), (0, 1)))

for k, v in PIPES.items():
    neigh = (
        (START[0] + v[0][0], START[1] + v[0][1]),
        (START[0] + v[1][0], START[1] + v[1][1]),
    )
    if sorted(start_n) == sorted(neigh):
        MAP[START] = k
        break

SNAKE1 = [START, start_n[0]]
SNAKE2 = [START, start_n[1]]

while len(list(set(SNAKE1) & set(SNAKE2))) == 1:
    sn1 = get_neighs(*SNAKE1[-1], PIPES[MAP[SNAKE1[-1]]])
    sn2 = get_neighs(*SNAKE2[-1], PIPES[MAP[SNAKE2[-1]]])
    if not sn1[0] in SNAKE1:
        SNAKE1.append(sn1[0])
    else:
        SNAKE1.append(sn1[1])
    if not sn2[0] in SNAKE2:
        SNAKE2.append(sn2[0])
    else:
        SNAKE2.append(sn2[1])

print(len(SNAKE1) - 1, len(SNAKE2) - 1)

# part 2

path = SNAKE1[1:] + SNAKE2[::-1]  # if negative result flip 1 and 2
shoelace = path + [path[0]]

area = 0
for a, b in zip(shoelace, shoelace[1:]):
    area += (a[0] * b[1]) - (a[1] * b[0])

print(int(area / 2 - len(path) // 2 + 1))
