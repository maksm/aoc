day = 3

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

line = lines[0]

map = {'>': 1, '^': 1j, '<': -1, 'v': -1j}
visited = set()
cur = 0
visited.add(cur)
for ch in line:
    cur += map[ch]
    visited.add(cur)
print(len(visited))

# part 2

# line = '^>v<' test

visited = set()
cur_s = 0
cur_r = 0
visited.add(cur_s)
for i, ch in enumerate(line):
    if i % 2 == 0:
        cur_s += map[ch]
        visited.add(cur_s)
    else:
        cur_r += map[ch]
        visited.add(cur_r)
print(len(visited))