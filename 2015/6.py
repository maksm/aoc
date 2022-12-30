import re

day = 6

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read()#.splitlines()

#lines = ['turn on 0,0 through 0,0']

lights = set()
for line in lines.splitlines():
    commands = re.findall(r'turn on|turn off|toggle', line)
    command = commands[0]

    numbers = re.findall(r'\d+', line)
    x0 = int(numbers[0])
    y0 = int(numbers[1])
    x1 = int(numbers[2])
    y1 = int(numbers[3])
    for i in range (x0, x1+1):
        for j in range(y0, y1+1):
            cur = i + j * 1j
            if command in ('turn on', 'toggle') and cur not in lights:
                lights.add(cur)
            elif command in ('turn off', 'toggle') and cur in lights:
                lights.remove(cur)
print(len(lights))

# # part 2
from datetime import datetime, timedelta

t0 = datetime.now()
lights = {}
for line in lines.splitlines():
    commands = re.findall(r'turn on|turn off|toggle', line)
    command = commands[0]

    numbers = re.findall(r'\d+', line)
    x0 = int(numbers[0])
    y0 = int(numbers[1])
    x1 = int(numbers[2])
    y1 = int(numbers[3])
    for i in range (x0, x1+1):
        for j in range(y0, y1+1):
            cur = i + j * 1j
            if cur not in lights:
                lights[cur] = 0
            if command == 'turn on':
                lights[cur] += 1
            elif command == 'toggle':
                lights[cur] += 2
            elif command == 'turn off':
                lights[cur] -= 1
                if lights[cur] < 0:
                    lights[cur] = 0

print(sum(v for v in lights.values()))
print(datetime.now() - t0)

from re import findall

t0 = datetime.now()
actions = {
    'toggle': lambda x: x + 2,
    'turn on': lambda x: x + 1,
    'turn off': lambda x: x - 1 if x > 0 else 0
}
lights = [[0 for i in range(1000)] for j in range(1000)]
instructions = findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", lines)
for action, x1, y1, x2, y2 in instructions:
    coords = [(x, y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
    for x, y in coords:
        lights[x][y] = actions[action](lights[x][y])
print(sum(val for sublist in lights for val in sublist))
print(datetime.now() - t0)