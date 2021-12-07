def intersect(p1, p2, p3, p4):
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1*p1[0] + b1*p1[1]

    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    det = a1*b2 - a2*b1

    if(det == 0):
        return None
    else:
        x = (b2*c1 - b1*c2)/det
        y = (a1*c2 - a2*c1)/det
        return (x,y)

def horizvert(p1, p2):
    return p1[0] == p2[0] or p1[1] == p2[1]


lines = [l.strip() for l in open("input.txt").readlines()]

grid = [[0 for i in range(1000)] for j in range(1000)]

vlines = []
for l in lines:
    lst = l.split(' -> ')
    p1 = tuple(int(i) for i in lst[0].strip().split(','))
    p2 = tuple(int(i) for i in lst[1].strip().split(','))
    vlines.append((p1, p2))

pts = set()

for i in range(len(vlines)):
    if(horizvert(vlines[i][0], vlines[i][1])):
        if(vlines[i][0][0] == vlines[i][1][0]):
            l = min(vlines[i][0][1], vlines[i][1][1])
            r = max(vlines[i][0][1], vlines[i][1][1])
            for p in range(l,r+1):
                grid[vlines[i][0][0]][p]+=1
        elif(vlines[i][0][1] == vlines[i][1][1]):
            l = min(vlines[i][0][0], vlines[i][1][0])
            r = max(vlines[i][0][0], vlines[i][1][0])
            for p in range(l, r + 1):
                grid[p][vlines[i][0][1]] += 1

print(sum(sum(1 for i in j if i >= 2) for j in grid))