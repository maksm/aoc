day = 12

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

tests = [
    ('[1,2,3]', 6),
    ('{"a":2,"b":4}',6),
    ('[[[3]]]', 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ('[]', 0),
    ('{}', 0),
]

def evaluate_dict(x, ignore):
    s = 0
    if ignore and 'red' in x.values():
        return 0
    for k, v in x.items():
        if type(v) == int:
            s += v
        elif type(v) == dict:
            s += evaluate_dict(v, ignore)
        elif type(v) == list:
            s += evaulate_list(v, ignore)
    return s

def evaulate_list(x, ignore):
    s = 0
    for v in x:
        if type(v) == int:
            s += v
        elif type(v) == dict:
            s += evaluate_dict(v, ignore)
        elif type(v) == list:
            s += evaulate_list(v, ignore)
    return s 

x123 = None
def evaluate(line, ignore=False):
    exec(f'global x123; x123 = {line}')
    if type(x123) == dict:
        return evaluate_dict(x123, ignore)
    else:
        return evaulate_list(x123, ignore)

# for line, test_result in tests:
#     result = evaluate(line)
#     print(line, result == test_result)

print(evaluate(lines[0]))

print(evaluate(lines[0], True))