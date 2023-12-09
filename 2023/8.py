day = 8

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

# lines = test.splitlines()[1:]

NET = {}

INSTR = lines[0]
for line in lines[2:]:
    ls = line.split(" = ")
    ls1 = ls[1][1:-1].split(", ")
    NET[ls[0]] = (ls1[0], ls1[1])

s = 0
cur = "AAA"
while cur != "ZZZ":
    for ch in INSTR:
        if ch == "R":
            cur = NET[cur][1]
        else:
            cur = NET[cur][0]
        s += 1
print(s)

# part 2

test = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

# lines = test.splitlines()[1:]

NET = {}

INSTR = lines[0]
for line in lines[2:]:
    ls = line.split(" = ")
    ls1 = ls[1][1:-1].split(", ")
    NET[ls[0]] = (ls1[0], ls1[1])

curs = [key for key in NET.keys() if key[-1] == "A"]

cycles = []
for cur in curs:
    s = 0
    while cur[-1] != "Z":
        for ch in INSTR:
            if ch == "R":
                cur = NET[cur][1]
            else:
                cur = NET[cur][0]
            s += 1
    cycles.append(s)

import math

print("part 2: ", math.lcm(*cycles))
