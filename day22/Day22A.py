lines = [l.strip() for l in open("input.txt").readlines()]

on = set()

for l in lines:
    a = l.split()[0].strip()
    b = l.split()[1]
    nums = b.split(',')
    xb = None
    yb = None
    zb = None
    for idx, num in enumerate(nums):
        vals = num.split('=')[1].split('..')
        if idx == 0:
            xb = [int(vals[0]), int(vals[1])]
        elif idx == 1:
            yb = [int(vals[0]), int(vals[1])]
        elif idx == 2:
            zb = [int(vals[0]), int(vals[1])]
    xb[0] = max(-50, xb[0])
    xb[1] = min(50, xb[1])
    yb[0] = max(-50, yb[0])
    yb[1] = min(50, yb[1])
    zb[0] = max(-50, zb[0])
    zb[1] = min(50, zb[1])
    for x in range(xb[0], xb[1]+1):
        for y in range(yb[0], yb[1]+1):
            for z in range(zb[0], zb[1]+1):
                if a == 'on':
                    on.add((x,y,z))
                else:
                    if (x,y,z) in on: on.remove((x,y,z))
print(len(on))