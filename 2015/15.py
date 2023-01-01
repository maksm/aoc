day = 15

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

test = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''

#lines = test.splitlines()

specs = {}
for i, line in enumerate(lines):
    ls = line.split(': ')
    specs[i] = {}
    for lss in ls[1].split(', '):
        k, v = lss.split()
        specs[i][k] = int(v)

def evaluate_recipe(recipe):
    scores = {}
    for i, count in enumerate(recipe):
        for attr, val in specs[i].items():
            if attr == 'calories':
                continue
            if attr not in scores:
                scores[attr] = 0
            scores[attr] += val*count
    score = 1
    for v in scores.values():
        score *= max(0, v)
    return score

best = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            l = 100 - i - j - k
            if l < 0 or i + j + k + l != 100:
                continue
            s = evaluate_recipe((i, j, k, l))
            best = max(best, s)

print(best)

#part 2
best = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            l = 100 - i - j - k
            if l < 0 or i + j + k + l != 100:
                continue
            recipe = (i, j, k, l)
            if sum(specs[m]['calories']*recipe[m] for m in range(len(specs))) != 500:
                continue
            s = evaluate_recipe(recipe)
            best = max(best, s)

print(best)