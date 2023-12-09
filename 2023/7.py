from collections import Counter

day = 7

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

# lines = test.splitlines()[1:]

ORDR_MAP = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

ORDR_HAND_MAP = {
    (5,): 5,
    (4, 1): 4,
    (3, 2): 3,
    (3, 1, 1): 2,
    (2, 2, 1): 1,
    (2, 1, 1, 1): 0,
    (1, 1, 1, 1, 1): -1,
}


def get_ordr(hnd):
    v = 0
    for i, ch in enumerate(hnd[::-1]):
        v += 15**i * (int(ch) if ch.isnumeric() else ORDR_MAP[ch])
    return v


hands = []
for line in lines:
    ls = line.split()
    hnd = ls[0]
    hnd_cnt = sorted(list(Counter(hnd).values()), reverse=True)
    stk = int(ls[1])
    ordr = get_ordr(hnd)
    hnd_ordr = ORDR_HAND_MAP[tuple(hnd_cnt)]
    hands.append((hnd, hnd_cnt, stk, hnd_ordr, ordr))

s = 0
for r, hand in enumerate(sorted(hands, key=lambda x: (x[-2], x[-1]))):
    s += (r + 1) * hand[2]
print("part 1: ", s)

# part 2

ORDR_MAP["J"] = 1

hands = []
for line in lines:
    ls = line.split()
    hnd = ls[0]
    hnd_cnt = sorted(list(Counter(hnd.replace("J", "")).values()), reverse=True)
    if len(hnd_cnt) > 0:
        hnd_cnt[0] += hnd.count("J")
    else:
        hnd_cnt = (5,)
    stk = int(ls[1])
    ordr = get_ordr(hnd)
    hnd_ordr = ORDR_HAND_MAP[tuple(hnd_cnt)]
    hands.append((hnd, hnd_cnt, stk, hnd_ordr, ordr))

s = 0
for r, hand in enumerate(sorted(hands, key=lambda x: (x[-2], x[-1]))):
    s += (r + 1) * hand[2]
print("part 2: ", s)
