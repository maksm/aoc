day = 14

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

test = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

# lines = test.splitlines()

specs = {}
for line in lines:
    ls = line.split()
    specs[ls[0]] = {
        "speed": int(ls[3]),
        "flight_time": int(ls[6]),
        "rest_time": int(ls[13]),
    }


def eval_flight(spec, t):
    s = 0
    cycle_time = spec["flight_time"] + spec["rest_time"]
    s += (t // cycle_time) * spec["flight_time"] * spec["speed"]
    tmin = min(t % cycle_time, spec["flight_time"])
    s += tmin * spec["speed"]
    return s


smax = 0
for k, v in specs.items():
    s = eval_flight(v, 2503)
    # print(k, s)
    smax = max(smax, s)

print(smax)

# part 2

for k in specs.keys():
    specs[k]["score"] = 0
    specs[k]["cur"] = 0

for t in range(2503):
    for k, v in specs.items():
        cycle_time = v["flight_time"] + v["rest_time"]
        if t % cycle_time < v["flight_time"]:
            v["cur"] += v["speed"]

    b = 0
    for v in sorted(specs.values(), key=lambda x: x["cur"], reverse=True):
        if b <= v["cur"]:
            b = v["cur"]
            v["score"] += 1
            continue
        break

print(sorted([v["score"] for k, v in specs.items()], reverse=True)[0])
