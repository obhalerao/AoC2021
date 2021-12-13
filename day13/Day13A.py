lines = [l.strip() for l in open("input.txt").readlines()]

points = set()
idx = 0
while lines[idx] != '':
    tmp = lines[idx].split(',')
    points.add((int(tmp[0]), int(tmp[1])))
    idx+=1

idx+=1
instr = lines[idx].split()[2]
a = instr.split('=')[0]
b = int(instr.split('=')[1])

npts = set()
if a == 'x':
    for pt in points:
        val = pt[0]
        if val < b:
            npts.add((val, pt[1]))
        else:
            npts.add((b-(val-b), pt[1]))
else:
    for pt in points:
        val = pt[1]
        if val < b:
            npts.add((pt[0], val))
        else:
            npts.add((pt[0], b-(val-b)))
print(len(npts))
