day = 18

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

test = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''

#lines = test.splitlines()

NEIGHS = (1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j)

lights = {}
for j, line in enumerate(lines):
    for i, ch in enumerate(line):
        lights[i + j*1j] = ch

def print_lights(lights):
    for j in range(6):
        line = ''
        for i in range(6):
            if i + j*1j in lights and lights[i + j*1j] == '#':
                line += '#'
            else:
                line += '.'
        print(line)
    print()

def cycle(lights, stuck=None):
    new_lights = {}
    for index, light in lights.items():
        neighs = [neigh for neigh in NEIGHS if neigh+index in lights and lights[neigh+index] == '#']
        new_lights[index] = light
        if stuck and index in stuck:
            continue
        if light == '#' and len(neighs) not in (2, 3):
            new_lights[index] = '.'
        elif light == '.' and len(neighs) == 3:
            new_lights[index] = '#'
    return new_lights

#print_lights(lights)
for i in range(100):
    new_lights = cycle(lights)
    if lights == new_lights:
        print(f'endgame after {i} cycles')
        break
    lights = new_lights
    #print_lights(lights)
print(len([v for v in lights.values() if v == '#']))

# part 2

lights = {}
for j, line in enumerate(lines):
    for i, ch in enumerate(line):
        lights[i + j*1j] = ch
ll = len(lines)-1
ll0 = len(lines[0])-1
stuck = (0, ll, ll0*1j, ll +  ll0*1j)
for s in stuck:
    lights[s] = '#'

for i in range(100):
    new_lights = cycle(lights, stuck)
    if lights == new_lights:
        print(f'endgame after {i} cycles')
        break
    lights = new_lights
print(len([v for v in lights.values() if v == '#']))
