lines = [l.strip() for l in open("input.txt").readlines()]

vals = [int(i) for i in lines[0].split(',')]

cmin = float("inf")
for idx in range(2000):
    dmin=0
    for j in range(len(vals)):
        v = abs(idx-vals[j])
        dmin+=((v*(v+1))//2)
    cmin = min(cmin, dmin)
print(cmin)