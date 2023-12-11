lines = open(f"2023/inputs/11.txt", "r").read().splitlines()

test = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

# lines = test.splitlines()[1:]

M = set()
xs = set()
ys = set()
for j, line in enumerate(lines):
    for i, ch in enumerate(line):
        if ch == "#":
            M.add((i, j))
            xs.add(i)
            ys.add(j)

xs = sorted(list(xs))
ys = sorted(list(ys))

xpand = [x for x in range(xs[0], xs[-1] + 1) if x not in xs]
ypand = [y for y in range(ys[0], ys[-1] + 1) if y not in ys]

for x in xpand[::-1]:
    N = set()
    R = set()
    for i, j in M:
        if i > x:
            R.add((i, j))
            N.add((i + 1, j))
    M = M.difference(R).union(N)

for y in ypand[::-1]:
    N = set()
    R = set()
    for i, j in M:
        if j > y:
            R.add((i, j))
            N.add((i, j + 1))
    M = M.difference(R).union(N)


def get_dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


MS = sorted(M)
k = 1
s = 0
for i, j in MS:
    for i1, j1 in MS[k:]:
        s += get_dist(i, j, i1, j1)
    k += 1
print(s)


# part 2
M = set()
xs = set()
ys = set()
for j, line in enumerate(lines):
    for i, ch in enumerate(line):
        if ch == "#":
            M.add((i, j))
            xs.add(i)
            ys.add(j)

xs = sorted(list(xs))
ys = sorted(list(ys))

xpand = [x for x in range(xs[0], xs[-1] + 1) if x not in xs]
ypand = [y for y in range(ys[0], ys[-1] + 1) if y not in ys]

for x in xpand[::-1]:
    N = set()
    R = set()
    for i, j in M:
        if i > x:
            R.add((i, j))
            N.add((i + 1000000 - 1, j))
    M = M.difference(R).union(N)

for y in ypand[::-1]:
    N = set()
    R = set()
    for i, j in M:
        if j > y:
            R.add((i, j))
            N.add((i, j + 1000000 - 1))
    M = M.difference(R).union(N)


def get_dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


MS = sorted(M)
k = 1
s = 0
for i, j in MS:
    for i1, j1 in MS[k:]:
        s += get_dist(i, j, i1, j1)
    k += 1
print(s)
