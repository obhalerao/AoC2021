lines = [l.strip() for l in open("input.txt").readlines()]

def inArea(x, y, x1, y1, x2, y2):
    return (x1 <= x) and (x <= x2) and (y1 <= y) and (y <= y2)

def invalid(x, y, x1, y1, x2, y2):
    return x > x2

def simulate(vx, vy, x1, y1, x2, y2):
    x = 0
    y = 0
    steps = 0
    maxy = -float("inf")
    while not invalid(x, y, x1, y1, x2, y2):
        if inArea(x, y, x1, y1, x2, y2):
            return True, maxy
        x+=vx
        y+=vy
        maxy = max(y, maxy)
        vx = max(0, vx-1)
        vy-=1
        steps+=1
        if steps > 1000:
            break
    return False, -1

lines[0] = lines[0].split('target area: ')[1]

inp = lines[0].split(', ')
inpx = inp[0].split('..')
inpx[0] = inpx[0][2:]
inpy = inp[1].split('..')
inpy[0] = inpy[0][2:]
x1 = int(inpx[0])
x2 = int(inpx[1])
y1 = int(inpy[0])
y2 = int(inpy[1])

res = -float("inf")

cnt = 0

for vy in range(0, 1000):
    for vx in range(100):
        ans = simulate(vx, vy, x1, y1, x2, y2)
        if ans[0]:
            res = max(res, ans[1])

print(res)