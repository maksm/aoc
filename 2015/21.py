from itertools import product, combinations

shop = {
    'Weapons': {
        'Dagger': {'Cost': 8, 'Damage': 4, 'Armor': 0},
        'Shortsword': {'Cost': 10, 'Damage': 5, 'Armor': 0},
        'Warhammer': {'Cost': 25, 'Damage': 6, 'Armor': 0},
        'Longsword': {'Cost': 40, 'Damage': 7, 'Armor': 0},
        'Greataxe': {'Cost': 74, 'Damage': 8, 'Armor': 0},
    },
    'Armor': {
        'Leather': {'Cost': 13, 'Damage': 0, 'Armor': 1},
        'Chainmail': {'Cost': 31, 'Damage': 0, 'Armor': 2},
        'Splintmail': {'Cost': 53, 'Damage': 0, 'Armor': 3},
        'Bandedmail': {'Cost': 75, 'Damage': 0, 'Armor': 4},
        'Platemail': {'Cost': 102, 'Damage': 0, 'Armor': 5},
        None: {'Cost': 0, 'Damage': 0, 'Armor': 0}
    },
    'Rings': {
        'Damage +1': {'Cost': 25, 'Damage': 1, 'Armor': 0},
        'Damage +2': {'Cost': 50, 'Damage': 2, 'Armor': 0},
        'Damage +3': {'Cost': 100, 'Damage': 3, 'Armor': 0},
        'Defense +1': {'Cost': 20, 'Damage': 0, 'Armor': 1},
        'Defense +2': {'Cost': 40, 'Damage': 0, 'Armor': 2},
        'Defense +3': {'Cost': 80, 'Damage': 0, 'Armor': 3},
        None: {'Cost': 0, 'Damage': 0, 'Armor': 0}
    },
}

boss = {'hp': 103, 'dmg': 9, 'arm': 2}

w = list(shop['Weapons'].keys())
a = list(shop['Armor'].keys()) + [None]
r = [c for c in combinations(list(shop['Rings']) + [None], 2)] + [(None, None)]

def fight_boss(w, a, r1, r2):
    hp = 100
    cost = shop['Weapons'][w]['Cost'] + shop['Armor'][a]['Cost'] + shop['Rings'][r1]['Cost'] + shop['Rings'][r2]['Cost']
    dmg = shop['Weapons'][w]['Damage'] + shop['Armor'][a]['Damage'] + shop['Rings'][r1]['Damage'] + shop['Rings'][r2]['Damage']
    arm = shop['Weapons'][w]['Armor'] + shop['Armor'][a]['Armor'] + shop['Rings'][r1]['Armor'] + shop['Rings'][r2]['Armor']
    ukillboss = boss['hp'] // max(1, dmg - boss['arm'])
    if boss['hp'] % max(1, dmg - boss['arm']) != 0:
        ukillboss += 1
    bosskillu = hp // max(1, boss['dmg'] - arm)
    if hp % max(1, boss['dmg'] - arm) != 0:
        bosskillu += 1
    return ukillboss <= bosskillu, cost

max_cost = 0
min_cost = float('inf')
for w, a, (r1, r2) in product(w, a, r):
    ukillboss, cost = fight_boss(w, a, r1, r2)
    if ukillboss and cost < min_cost:
        min_cost = cost
    if not ukillboss and cost > max_cost:
        max_cost = cost

print(min_cost)
print(max_cost)
