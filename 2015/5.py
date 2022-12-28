day = 5

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

bad = ('ab', 'cd', 'pq', 'xy')

tests = [
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', False),
    ('haegwjzuvuyypxyu', False),
    ('dvszwmarrgswjxmb', False)
]

s = 0
for line in lines:
    if (not any(b in line for b in bad) 
    and sum([line.count(a) for a in 'aeiou']) > 2 
    and any(line[i-1]==line[i] for i in range(len(line)))):
        #print(line, test == True)
        s += 1
    #else:
    #    print(line, test == False)
print(s)