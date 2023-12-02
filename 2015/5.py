day = 5

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

bad = ("ab", "cd", "pq", "xy")

tests = [
    ("ugknbfddgicrmopn", True),
    ("ugknbfddgucrmopn", True),
    ("aaa", True),
    ("jchzalrnumimnmhp", False),
    ("haegwjzuvuyypxyu", False),
    ("dvszwmarrgswjxmb", False),
    ("xesxgeaucmhswnex", False),
    ("dovxcywlyvspixad", False),
    ("ylnyuloaukdrhwuy", False),
    ("njtzlceyevmisxfn", False),
    ("puoagefcmlxelvlp", False),
]


s = 0
for line in lines:
    if (
        not any(b in line for b in bad)
        and sum([line.count(a) for a in "aeiou"]) > 2
        and any(line[i - 1] == line[i] for i in range(1, len(line)))
    ):
        # print(line, test == True)
        s += 1
    # else:
    #    print(line, test == False)
print(s)

tests2 = [
    ("qjhvhtzxzqqjkmpb", True),
    ("xxyxx", True),
    ("uurcxstgmygtbstg", False),
    ("ieodomkazucvgmuy", False),
]

s = 0
for line in lines:
    if any(
        line.count(line[i - 1 : i + 1]) > 1 for i in range(1, len(line) - 1)
    ) and any(line[i - 1] == line[i + 1] for i in range(1, len(line) - 1)):
        s += 1
        # print(line, test == True)
    # else:
    #    print(line, test == False)
print(s)
