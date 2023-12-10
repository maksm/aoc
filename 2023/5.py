day = 5

seeds, *maps = open(f"2023/inputs/{day}.txt", "r").read().split("\n\n")


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

# seeds, *maps = test.split("\n\n")

seeds = [int(seed) for seed in seeds.split()[1:]]
maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]

s0 = 1000000000000000000
for x in seeds:
    for m in maps:
        y = x
        for d, s, r in m:
            if s <= x < s + r:
                y = d + (x - s)
                break
        x = y
    s0 = min(s0, y)
print(s0)

# part 2

locations = []
for i in range(0, len(seeds), 2):
    ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
    results = []
    for m in maps:
        while ranges:
            sr, er = ranges.pop()
            for d, s, r in m:
                em = s + r
                n = d - s
                if em <= sr or er <= s:  # no overlap
                    continue
                if sr < s:
                    ranges.append([sr, s])
                    sr = s
                if em < er:
                    ranges.append([em, er])
                    er = em
                results.append([sr + n, er + n])
                break
            else:
                results.append([sr, er])
        ranges = results
        results = []
    locations += ranges
print(min(loc[0] for loc in locations))
