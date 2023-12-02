day = 7

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


binary_python_operations_map_and_python_reserved_keywords = {
    #   '->': '=',
    "AND": "&",
    "OR": "|",
    "NOT": "~",
    "LSHIFT": "<<",
    "RSHIFT": ">>",
    "as": "ass",
    "in": "inn",
    "is": "iss",
    "if": "iff",
    "or": "orr",
}

# lines = test.splitlines()

to_run = []
for line in lines:
    for (
        change_frm,
        change_to,
    ) in binary_python_operations_map_and_python_reserved_keywords.items():
        line = line.replace(change_frm, change_to)
    linesplit = line.split(" -> ")
    to_run.append(linesplit[1] + " = " + linesplit[0])

while to_run:
    next_line = to_run.pop(0)
    try:
        exec(next_line)
    except:
        to_run.append(next_line)
        continue
    print(f"evaluated line {next_line} and {len(to_run)} remaining")

print(a)
