day = 2

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

test = ('2x3x4', 58, 34)
test2 = ('1x1x10', 43, 14)

for line, answer, _ in (test, test2):
    l, w, h = [int(x) for x in line.split('x')]
    sa = 2*l*w + 2*w*h + 2*h*l
    sl = min(l*w, w*h, h*l)
    print(line, sa+sl, answer)
print()

s = 0
for line in lines:
    l, w, h = [int(x) for x in line.split('x')]
    sa = 2*l*w + 2*w*h + 2*h*l
    sl = min(l*w, w*h, h*l)
    s += sa + sl
print(s)
print()

#part 2
for line, _, answer in (test, test2):
    l, w, h = [int(x) for x in line.split('x')]
    sa = l*w*h
    sl = sorted([l, w, h])
    print(line, sa+2*sl[0]+2*sl[1], answer)
print()

s = 0
for line in lines:
    l, w, h = [int(x) for x in line.split('x')]
    sa = l*w*h
    sl = sorted([l, w, h])
    s += sa+2*sl[0]+2*sl[1]
print(s)
