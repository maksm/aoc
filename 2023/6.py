day = 6

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
Time:      7  15   30
Distance:  9  40  200
"""

# lines = test.splitlines()[1:]

times = list(map(int, lines[0].split(": ")[1].split()))
records = list(map(int, lines[1].split(": ")[1].split()))

s = 1
for i, T in enumerate(times):
    s0 = 0
    for v in range(1, T):
        if (T - v) * v > records[i]:
            s0 += 1
    s *= s0
print(s)

# part 2

time = int("".join(lines[0].split(": ")[1].split()))
record = int("".join(lines[1].split(": ")[1].split()))
s0 = 0
for v in range(1, time):
    if (time - v) * v > record:
        s0 += 1
print(s0)
