day = 1

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()


def count_floor(line):
    return sum(1 for x in line if x == "(") + sum(-1 for x in line if x == ")")


# part 1
print(count_floor(lines[0]))

# part 2
i = 1
line = lines[0]
while (
    sum(1 for x in line[:i] if x == "(") + sum(-1 for x in line[:i] if x == ")") != -1
):
    i += 1

print(i)
