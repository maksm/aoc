day = 10

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

test = '1'

#line = test
line = lines[0]

for i in range(50):
    result = ''
    cnt = 0
    cur = line[0]
    for ch in line:
        if cur == ch:
            cnt += 1
        else:
            result += f'{cnt}{cur}'
            cur = ch
            cnt = 1
    result += f'{cnt}{cur}'
    line = result
print(len(result))