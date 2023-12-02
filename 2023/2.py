day = 2

with open(f"2023/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

# lines = test.splitlines()[1:]

CC = {"red": 12, "green": 13, "blue": 14}

s = 0
for line in lines:
    ls = line.split(": ")
    g = int(ls[0].split()[1])
    valid = True
    for game in ls[1].split("; "):
        for color in game.split(", "):
            gs = color.split()
            if int(gs[0]) > CC[gs[1]]:
                valid = False
                break
    if valid:
        print(f"Game {g} is valid")
        s += g
print(s)

# part 2

s = 0
for line in lines:
    ls = line.split(": ")
    g = int(ls[0].split()[1])
    mg = {"red": 0, "green": 0, "blue": 0}
    for game in ls[1].split("; "):
        for color in game.split(", "):
            gs = color.split()
            if int(gs[0]) > mg[gs[1]]:
                mg[gs[1]] = int(gs[0])
    s += mg["red"] * mg["green"] * mg["blue"]
print(s)
