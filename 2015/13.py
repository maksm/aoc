day = 13

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

# lines = test.splitlines()

gains = {}

for line in lines:
    ls = line.split()
    if ls[0] not in gains:
        gains[ls[0]] = {}
    gains[ls[0]][ls[-1][:-1]] = int(ls[3]) if ls[2] == "gain" else -int(ls[3])

from itertools import permutations


def evaluate_table(table):
    s = 0
    prev = table[-1]
    for i in range(len(table)):
        s += gains[table[i]][prev] + gains[prev][table[i]]
        prev = table[i]
    return s


score = 0
for table in permutations(gains.keys()):
    score = max(score, evaluate_table(table))

print(score)

# part 2

gains["me"] = {}
for k in gains.keys():
    gains["me"][k] = 0
    gains[k]["me"] = 0
score = 0
for table in permutations(gains.keys()):
    score = max(score, evaluate_table(table))

print(score)
