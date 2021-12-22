lines = [l.strip() for l in open("input.txt").readlines()]

def getLines(a, b):
    if b[0] <= a[0] and b[1] >= a[1]:
        return [(a[0], a[1])]
    elif b[1] < a[0] or b[0] > a[1]:
        return [(a[0], a[1])]
    elif b[0] > a[0] and b[1] < a[1]:
        return [(a[0], b[0]-1), (b[0], b[1]), (b[1]+1, a[1])]
    elif b[0] <= a[0] and b[1] < a[1]:
        return [(a[0], b[1]), (b[1]+1, a[1])]
    elif b[0] > a[0] and b[1] >= a[1]:
        return [(a[0], b[0]-1), (b[0], a[1])]

def intersection(a, b):
    if b[0] <= a[0] and b[1] >= a[1]:
        return (a[0], a[1])
    elif b[1] < a[0] or b[0] > a[1]:
        return None
    elif b[0] > a[0] and b[1] < a[1]:
        return (b[0], b[1])
    elif b[0] <= a[0] and b[1] < a[1]:
        return (a[0], b[1])
    elif b[0] > a[0] and b[1] >= a[1]:
        return (b[0], a[1])

def difference(a, b):
    results = []
    xd = getLines(a[0], b[0])
    yd = getLines(a[1], b[1])
    zd = getLines(a[2], b[2])
    ix = intersection(a[0], b[0])
    iy = intersection(a[1], b[1])
    iz = intersection(a[2], b[2])
    for x in xd:
        for y in yd:
            for z in zd:
                if x != ix or y != iy or z != iz:
                    results.append((x,y,z))
    return results

def cuboids(a, b):
    results = a.copy()
    for diff in b:
        nresults = []
        for cb in results:
            nk = difference(cb, diff)
            for i in nk:
                nresults.append(i)
        results = nresults
    return results

def consolidate(a,b):
    if a[0] == b[0] and a[1] == b[1] and a[2][1]+1 == b[2][0]:
        return (a[0], a[1], (a[2][0], b[2][1]))
    elif a[0] == b[0] and a[1] == b[1] and b[2][1]+1 == a[2][0]:
        return (a[0], a[1], (b[2][0], a[2][1]))
    elif a[0] == b[0] and a[2] == b[2] and a[1][1]+1 == b[1][0]:
        return (a[0], (a[1][0], b[1][1]), a[2])
    elif a[0] == b[0] and a[2] == b[2] and b[1][1]+1 == a[1][0]:
        return (a[0], (b[1][0], a[1][1]), a[2])
    elif a[2] == b[2] and a[1] == b[1] and a[0][1]+1 == b[0][0]:
        return ((a[0][0], b[0][1]), a[1], a[2])
    elif a[2] == b[2] and a[1] == b[1] and b[0][1]+1 == a[0][0]:
        return ((b[0][0], a[0][1]), a[1], a[2])
    return None

on = []

for iii, l in enumerate(lines):
    a = l.split()[0].strip()
    b = l.split()[1]
    nums = b.split(',')
    xb = None
    yb = None
    zb = None
    for idx, num in enumerate(nums):
        vals = num.split('=')[1].split('..')
        if idx == 0:
            xb = (int(vals[0]), int(vals[1]))
        elif idx == 1:
            yb = (int(vals[0]), int(vals[1]))
        elif idx == 2:
            zb = (int(vals[0]), int(vals[1]))

    item = (xb,yb,zb)
    print(iii, len(on))
    if a == 'on':
        non = cuboids([item], on)
        for i in non:
            on.append(i)
    else:
        on = cuboids(on, [item])
    for iter in range(10):
        newon = []
        consolidated = [False for i in range(len(on))]
        for idx, i in enumerate(on):
            for idx2, j in enumerate(on):
                if idx == idx2:
                    continue
                if consolidated[idx] or consolidated[idx2]:
                    continue
                results = consolidate(i,j)
                if results:
                    consolidated[idx] = True
                    consolidated[idx2] = True
                    newon.append(results)
        if not any(consolidated):
            break
        for idx, i in enumerate(consolidated):
            if not i:
                newon.append(on[idx])
        on = newon


cnt = 0
for i in on:
    cnt+=((i[0][1]-i[0][0]+1)*(i[1][1]-i[1][0]+1)*(i[2][1]-i[2][0]+1))
print(cnt)