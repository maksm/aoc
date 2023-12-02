with open("1.txt") as f:
    lines = f.readlines()

s = 0
for line in lines:
    first = None
    last = None
    for ch in line:
        if ch.isnumeric():
            if not first:
                first = ch
            last = ch
    s += int(first + last)

print(s)

# part 2

with open("1.txt") as f:
    lines = f.readlines()

W2N = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

s = 0
for line in lines:
    first = None
    last = None
    for i, ch in enumerate(line):
        if ch.isnumeric():
            if not first:
                first = ch
            last = ch
        else:
            for w, n in W2N.items():
                if i + len(w) > len(line):
                    continue
                if line[i : i + len(w)] == w:
                    if not first:
                        first = str(n)
                    last = str(n)
                    break
    s += int(first + last)
print(s)
