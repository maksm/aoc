day = 1

with open(f"2016/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = "R8, R4, R4, R8"

line = test
line = lines[0]

pos = 0 + 0j
rot = 0 + 1j
for inst in line.split(", "):
    if inst[0] == "R":
        rot = rot.imag - rot.real * 1j
    else:
        rot = -rot.imag + rot.real * 1j
    for j in range(int(inst[1:])):
        pos += rot
print(pos)
print(abs(pos.real) + abs(pos.imag))

# part 2
pos = 0 + 0j
rot = 0 + 1j
visited = set()
visited.add(pos)
for inst in line.split(", "):
    if inst[0] == "R":
        rot = rot.imag - rot.real * 1j
    else:
        rot = -rot.imag + rot.real * 1j
    for j in range(int(inst[1:])):
        pos += rot
        if pos in visited:
            print(pos)
            print(abs(pos.real) + abs(pos.imag))
            break
        visited.add(pos)
    else:
        continue
    break
