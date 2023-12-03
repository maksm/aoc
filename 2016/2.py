day = 2

with open(f"2016/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """"
ULL
RRDDD
LURDL
UUUUD
"""

# lines = test.splitlines()[1:]

GRID = {
    0 + 0j: "1",
    1 + 0j: "2",
    2 + 0j: "3",
    0 + 1j: "4",
    1 + 1j: "5",
    2 + 1j: "6",
    0 + 2j: "7",
    1 + 2j: "8",
    2 + 2j: "9",
}

MOVE = {"U": -1j, "D": 1j, "L": -1, "R": 1}

pos = 1 + 1j
code = ""
for line in lines:
    for ch in line:
        next_pos = pos + MOVE[ch]
        if next_pos in GRID:
            pos = next_pos
    code += GRID[pos]
print(code)

# part 2

GRID = {
    2: 1,
    1 + 1j: "2",
    2 + 1j: "3",
    3 + 1j: "4",
    2j: "5",
    1 + 2j: "6",
    2 + 2j: "7",
    3 + 2j: "8",
    4 + 2j: "9",
    1 + 3j: "A",
    2 + 3j: "B",
    3 + 3j: "C",
    2 + 4j: "D",
}

pos = 2j
code = ""
for line in lines:
    for ch in line:
        next_pos = pos + MOVE[ch]
        if next_pos in GRID:
            pos = next_pos
    code += str(GRID[pos])
print(code)
