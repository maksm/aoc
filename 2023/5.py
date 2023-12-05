day = 5

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

# lines = test.splitlines()[1:]

seeds = list(map(int, lines[0].split()[1:]))

maps = {}
k = None
for line in lines[2:]:
    if len(line) < 3:
        continue
    if line[0].isalpha():
        k = line.split()[0].split("-")
        if k[0] not in maps:
            maps[k[0]] = {}
        if k[2] not in maps[k[0]]:
            maps[k[0]][k[2]] = []
    else:
        maps[k[0]][k[2]].append(list(map(int, line.split())))

s0 = 1000000000000000000
for x in seeds:
    cur = "seed"
    next = None
    text = f"Seed {x},"
    while next != "location":
        next = list(maps[cur].keys())[0]
        y = x
        for d, s, r in maps[cur][next]:
            if s <= x < s + r:
                y = d + (x - s)
                break
        text += f" {next} {y},"
        x = y
        cur = next
    text = text[:-1] + "."
    s0 = min(s0, y)
print(s0)

# part 2

s0 = 1000000000000000000
for i in range(0, len(seeds), 2):
    print(seeds[i], seeds[i + 1], seeds[i] + seeds[i + 1])
    for j in range(seeds[i], seeds[i] + seeds[i + 1]):
        cur = "seed"
        next = None
        while next != "location":
            next = list(maps[cur].keys())[0]
            y = x
            for d, s, r in maps[cur][next]:
                if s <= x < s + r:
                    y = d + (x - s)
                    break
            x = y
            cur = next
        s0 = min(s0, y)
print(s0)
