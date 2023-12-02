day = 16

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

real_sue = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

real_sue = dict(
    [(line.split(": ")[0], int(line.split(": ")[1])) for line in real_sue.splitlines()]
)

all_sues = []
for i, line in enumerate(lines):
    cur_sue = {"num": i + 1}
    ls = line[line.find(": ") + 2 :].split(", ")
    for attr in ls:
        cur_sue[attr.split(": ")[0]] = int(attr.split(": ")[1])
    all_sues.append(cur_sue)

while len(all_sues) > 1:
    sue = all_sues.pop()
    if all(real_sue[attr] == val for attr, val in sue.items() if attr != "num"):
        all_sues.insert(0, sue)

print(all_sues[0]["num"])


# part 2
all_sues = []
for i, line in enumerate(lines):
    cur_sue = {"num": i + 1}
    ls = line[line.find(": ") + 2 :].split(", ")
    for attr in ls:
        cur_sue[attr.split(": ")[0]] = int(attr.split(": ")[1])
    all_sues.append(cur_sue)

while len(all_sues) > 1:
    sue = all_sues.pop()
    matches = True
    for k, v in sue.items():
        if k == "num":
            continue
        elif k in ("cats", "trees") and v <= real_sue[k]:
            matches = False
            break
        elif k in ("pomeranians", "goldfish") and v >= real_sue[k]:
            matches = False
            break
        elif k not in ("cats", "trees", "pomeranians", "goldfish") and v != real_sue[k]:
            matches = False
            break
    if matches:
        all_sues.insert(0, sue)

print(all_sues[0]["num"])
