day = 3

with open(f"2016/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = "5 10 25"

# lines = [test]

c = 0
for line in lines:
    ls = sorted(map(int, line.split()))
    if ls[0] + ls[1] > ls[2]:
        c += 1
print(c)

# part 2

test = """
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
"""

# lines = test.splitlines()[1:]

triplets = []
queue = []
for line in lines:
    ls = map(int, line.split())
    if len(queue) == 9:
        triplets.extend(
            [
                [queue[0], queue[3], queue[6]],
                [queue[1], queue[4], queue[7]],
                [queue[2], queue[5], queue[8]],
            ]
        )
        queue = []
    queue.extend(ls)
if len(queue) == 9:
    triplets.extend(
        [
            [queue[0], queue[3], queue[6]],
            [queue[1], queue[4], queue[7]],
            [queue[2], queue[5], queue[8]],
        ]
    )

c = 0
for tri in triplets:
    tri = sorted(tri)
    if tri[0] + tri[1] > tri[2]:
        c += 1
print(c)
