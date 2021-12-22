from array import array

lines = [l.strip() for l in open("input.txt").readlines()]

on = set()

coords = []

commands = []

results = [[[0 for i in range(900)] for j in range(900)] for k in range(900)]

for index, l in enumerate(lines):
    a = l.split()[0].strip()
    commands.append(a)
    b = l.split()[1]
    nums = b.split(',')
    xb = None
    yb = None
    zb = None
    for idx, num in enumerate(nums):
        vals = num.split('=')[1].split('..')
        if idx == 0:
            xb = [int(vals[0]), int(vals[1])+1]
        elif idx == 1:
            yb = [int(vals[0]), int(vals[1])+1]
        elif idx == 2:
            zb = [int(vals[0]), int(vals[1])+1]
    coord = (xb,yb,zb)
    for idx1, v in enumerate(coord):
        for idx2, w in enumerate(v):
            coords.append((w, index, idx1, idx2))

coords.sort()
xc = [i for i in coords if i[2] == 0]
yc = [i for i in coords if i[2] == 1]
zc = [i for i in coords if i[2] == 2]
xcoords = [[0 for i in range(2)] for k in range(len(lines))]
ycoords = [[0 for i in range(2)] for k in range(len(lines))]
zcoords = [[0 for i in range(2)] for k in range(len(lines))]
invx = []
invy = []
invz = []
for idx, i in enumerate(xc):
    index = i[1]
    dim = i[2]
    bd = i[3]
    if dim == 0: xcoords[index][bd] = idx
    invx.append(i[0])
for idx, i in enumerate(yc):
    index = i[1]
    dim = i[2]
    bd = i[3]
    if dim == 1: ycoords[index][bd] = idx
    invy.append(i[0])
for idx, i in enumerate(zc):
    index = i[1]
    dim = i[2]
    bd = i[3]
    if dim == 2: zcoords[index][bd] = idx
    invz.append(i[0])

for c in range(len(xcoords)):
    xb = xcoords[c]
    yb = ycoords[c]
    zb = zcoords[c]
    print(c)
    for x in range(xb[0], xb[1]):
        for y in range(yb[0], yb[1]):
            for z in range(zb[0], zb[1]):
                if commands[c] == 'on':
                    results[x][y][z] = True
                else:
                    results[x][y][z] = False

cnt = 0
for x in range(900):
    print(x)
    for y in range(900):
        for z in range(900):
            if not results[x][y][z]: continue
            ans=(invx[x+1]-invx[x])*(invy[y+1]-invy[y])*(invz[z+1]-invz[z])
            cnt+=ans
print(cnt)





