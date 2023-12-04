day = 4

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# lines = test.splitlines()[1:]

s = 0
for line in lines:
    ls = line.split(": ")
    cn = int(ls[0].split()[1])
    gs = ls[1].split(" | ")
    wn = set(map(int, gs[0].split()))
    pn = set(map(int, gs[1].split()))
    m = len(set(wn) & set(pn))
    if m > 0:
        s += 2 ** (m - 1)
print(s)

# part 2

copies = {}
for line in lines:
    ls = line.split(": ")
    cn = int(ls[0].split()[1])
    if cn not in copies:
        copies[cn] = 0
    copies[cn] += 1
    gs = ls[1].split(" | ")
    wn = set(map(int, gs[0].split()))
    pn = set(map(int, gs[1].split()))
    m = len(set(wn) & set(pn))
    for i in range(m):
        if cn + i + 1 not in copies:
            copies[cn + i + 1] = 0
        copies[cn + i + 1] += copies[cn]

s = 0
for k, v in copies.items():
    s += v
print(s)
