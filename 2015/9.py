day = 9

with open(f'2015/inputs/{day}.txt','r') as f: lines = f.read().splitlines()

test = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''

#lines = test.splitlines()

dists = {}
for line in lines:
    ls = line.split()
    if ls[0] not in dists:
        dists[ls[0]] = {}
    if ls[2] not in dists:
        dists[ls[2]] = {}
    dists[ls[0]][ls[2]] = int(ls[4])
    dists[ls[2]][ls[0]] = int(ls[4])

result = float('inf')
def hamilton_paths(graph, cur, path, calc_min=True):
    if len(path) == len(graph):
        #print(' -> '.join(path), sum(graph[path[i]][path[i+1]] for i in range(len(path)-1)))
        global result
        if calc_min:
            result = min(result, sum(graph[path[i]][path[i+1]] for i in range(len(path)-1)))
        else:
            result = max(result, sum(graph[path[i]][path[i+1]] for i in range(len(path)-1)))
        return
    for v in graph[cur].keys():
        if v not in path and (path or v not in graph[path[-1]].keys()):
            hamilton_paths(graph, cur, path + [v], calc_min)

for city in dists.keys():
    hamilton_paths(dists, city, [city])

print(result)

# part 2
result = 0
for city in dists.keys():
    hamilton_paths(dists, city, [city], False)

print(result)