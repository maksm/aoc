day = 8

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

#ESCAPE_SEQS = ['\\', '\"', '\x']

test = r'''""
"abc"
"aaa\"aaa"
"\x27"
'''

#lines = test.splitlines()

s = 0
for line in lines:
    #print(line, len(line), len(eval(line)))
    s += len(line)
    s -= len(eval(line))
print(s)

# part 2
s1 = s2 = 0
for line in lines:
    nline = '"'+line.replace('\\', r'\\').replace(r'"', r'\"')+'"'
    #print(len(nline), len(line), line, nline)
    s1 += len(nline)
    s2 += len(line)
print(s1 - s2)