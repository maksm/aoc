day = 19

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """H => HO
H => OH
O => HH

HOHOHO"""

# lines = test.splitlines()

specs = {}
orig = lines[-1]
for line in lines[:-2]:
    ls = line.split(" => ")
    if ls[0] not in specs:
        specs[ls[0]] = []
    specs[ls[0]].append(ls[1])


def get_variations(specs, orig):
    mols = set()
    for i in range(len(orig)):
        if orig[i] in specs:
            for var in specs[orig[i]]:
                mols.add((orig[:i] if i > 0 else "") + var + orig[i + 1 :])
        elif i < len(orig) - 1 and orig[i : i + 2] in specs:
            for var in specs[orig[i : i + 2]]:
                mols.add(orig[:i] + var + orig[i + 2 :])
    return mols


mols = get_variations(specs, orig)
print(len(mols))


# part 2

test = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO"""

# lines = test.splitlines()

specs = {}
reverse_specs = {}
target = lines[-1]
for line in lines[:-2]:
    ls = line.split(" => ")
    if ls[0] not in specs:
        specs[ls[0]] = []
    specs[ls[0]].append(ls[1])
    reverse_specs[ls[1]] = ls[0]


running_min = float("inf")


def process(specs, path, target):
    global running_min
    if len(path) - 1 > running_min:
        return float("inf")
    cur = path[-1]
    if cur == target:
        if running_min > len(path) - 1:
            # print(f'running_min {len(path)-1}')
            running_min = len(path) - 1
        return len(path) - 1
    if len(cur) >= len(target):
        return float("inf")
    cur_min = float("inf")
    for next in get_variations(specs, cur):
        val = process(specs, path + [next], target)
        cur_min = min(cur_min, val)
    return cur_min


# print(process(specs, ['e'], target))

rev_spec_ordered = sorted(
    list(reverse_specs.keys()), key=lambda x: len(x), reverse=True
)


def get_prev_mol(target):
    prev_mol = ""
    while target:
        # print(target, prev_mol)
        for rev_spec in rev_spec_ordered:
            if target[-len(rev_spec) :] == rev_spec:
                prev_mol = reverse_specs[rev_spec] + prev_mol
                target = target[: -len(rev_spec)]
                break
    return prev_mol


print(target)
for i in range(3):
    target = get_prev_mol(target)
    print(target)
    if "e" in target:
        print(i)
        break
