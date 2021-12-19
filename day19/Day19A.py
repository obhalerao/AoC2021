from itertools import permutations
from collections import deque

lines = [l.strip() for l in open("input.txt").readlines()]

EVENS = {0,3,4}

PERM_INVERSES = {(0,1,2):(0,1,2),
 (0,2,1):(0,2,1),
 (1,0,2):(1,0,2),
 (1,2,0):(2,0,1),
 (2,0,1):(1,2,0),
 (2,1,0):(2,1,0)}

def multiplier_generator(vals):
    for idx, perm in enumerate(permutations(vals)):
        if idx in EVENS:
            yield perm, (1,1,1)
            for i in range(3):
                ret = [-1,-1,-1]
                ret[i]*=-1
                yield perm, tuple(ret)
        else:
            yield perm, (-1,-1,-1)
            for i in range(3):
                ret = [1,1,1]
                ret[i]*=-1
                yield perm, tuple(ret)

ORIE = {}
for idx, (perm, mult) in enumerate(multiplier_generator((0,1,2))):
    ORIE[idx] = (perm, mult)

def convert(measurements, pos, orie):
    perm, mult = ORIE[orie]
    actuals = []
    for m in measurements:
        nm = tuple(m[perm[i]] for i in range(3))
        nm = tuple(mult[i]*nm[i] for i in range(3))
        actuals.append(tuple(nm[i]+pos[i] for i in range(3)))
    return actuals

def getPos(measurement, realPos, orie):
    global PERM_INVERSES
    perm, mult = ORIE[orie]
    nm = tuple(measurement[perm[i]] for i in range(3))
    nm = tuple(mult[i] * nm[i] for i in range(3))
    return tuple(realPos[i]-nm[i] for i in range(3))


coordinates = []
orientations = []
measurements = []

index = -1
for line in lines:
    if line[:2] == '--':
        index+=1
        measurements.append([])
        coordinates.append(None)
        orientations.append(None)
    elif line != '':
        vals = tuple((int(i) for i in line.split(',')))
        measurements[index].append(vals)

coordinates[0] = (0,0,0)
orientations[0] = 0

q = deque()
q.appendleft(0)


while not all(coordinates):
    idx = q.pop()
    actuals = convert(measurements[idx], coordinates[idx], orientations[idx])
    setactuals = set(actuals)
    print(idx)
    for scanner in range(len(coordinates)):
        if coordinates[scanner]:
            continue
        good = False
        for pt in measurements[scanner]:
            for pt2 in actuals:
                for orie in range(24):
                    tempPos = getPos(pt, pt2, orie)
                    ans = set(convert(measurements[scanner], tempPos, orie))
                    if len(ans & setactuals) >= 12:
                        coordinates[scanner] = tempPos
                        orientations[scanner] = orie
                        good = True
                        q.appendleft(scanner)
                        break
                if good: break
            if good: break

ans = set(convert(measurements[0], coordinates[0], orientations[0]))
for i in range(1, len(measurements)):
    cur = set(convert(measurements[i], coordinates[i], orientations[i]))
    ans = ans | cur
print(len(ans))




