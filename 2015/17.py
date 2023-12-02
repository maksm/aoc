day = 17

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = [20, 15, 10, 5, 5]

# buckets = test
target = 150
buckets = [int(x) for x in lines]

from itertools import combinations

combos = []
for i in range(4, len(buckets)):
    for combo in combinations(buckets, i):
        if sum(combo) == target:
            combos.append(combo)

print(len(combos))

combos = []
for i in range(4, 5):
    for combo in combinations(buckets, i):
        if sum(combo) == target:
            combos.append(combo)

print(len(combos))
