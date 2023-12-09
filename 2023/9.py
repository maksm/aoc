day = 9

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

# lines = test.splitlines()[1:]


def get_diff_seq(seq):
    return [seq[i] - seq[i - 1] for i in range(1, len(seq))]


s = 0
for line in lines:
    seq = list(map(int, line.split()))
    seq_lvls = []
    while not all(x == 0 for x in seq):
        seq_lvls.append(seq)
        seq = get_diff_seq(seq)
    next = 0
    for i, seq in enumerate(seq_lvls[::-1]):
        next += seq[-1]
    s += next
print(s)

# part 2

s = 0
for line in lines:
    seq = list(map(int, line.split()))
    seq_lvls = []
    while not all(x == 0 for x in seq):
        seq_lvls.append(seq)
        seq = get_diff_seq(seq)
    next = 0
    for i, seq in enumerate(seq_lvls[::-1]):
        next = seq[0] - next
    s += next
print(s)
