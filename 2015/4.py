import hashlib

day = 4

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

line = lines[0]

# line = 'abcdef' # test

for i in range(1, 1000000):
    s = line + str(i)
    hexmd5 = hashlib.md5(s.encode("utf-8")).hexdigest()
    if hexmd5[:5] == "00000":
        print(i, s, hexmd5)
        break

# part 2
for i in range(1, 10000000):
    s = line + str(i)
    hexmd5 = hashlib.md5(s.encode("utf-8")).hexdigest()
    if hexmd5[:6] == "000000":
        print(i, s, hexmd5)
        break
