import heapq

lines = [l.strip('\n') for l in open("input.txt").readlines()]

grid = [[i for i in line] for line in lines[1:-1]]

locations = [(0,1),(0,2),(0,4),(0,6),(0,8),(0,10),(0,11)]

FINAL = '''#...........#
###A#B#C#D###
  #A#B#C#D#'''

FINAL = tuple(tuple(i) for i in FINAL.split('\n'))

endlocations = {'A':[(1,3),(2,3)],
                'B':[(1,5),(2,5)],
                'C':[(1,7),(2,7)],
                'D':[(1,9),(2,9)]}

chars = {'A','B','C','D'}

costs = {'A':1,
         'B':10,
         'C':100,
         'D':1000}

INF = 10000000000

def energyCalc(c, op, np):
    global costs
    dist = abs(op[0]-np[0])+abs(op[1]-np[1])
    return costs[c]*dist

def good(grid):
    global endlocations
    return all(grid[k[0]][k[1]] == a for a,i in endlocations.items() for k in i)

dists = {}
seen = set()

arr = [(0, tuple(tuple(g) for g in grid))]
heapq.heapify(arr)
while arr:
    temp = heapq.heappop(arr)
    energy = temp[0]
    grid = temp[1]
    if len(seen) % 10000 == 0:
        print(len(seen))
    if grid in seen:
        continue
    seen.add(grid)
    grid = [list(i) for i in grid]
    if(good(grid)):
        break
    inarr = []
    for j in locations:
        if grid[j[0]][j[1]] != '.':
            inarr.append(j[1])
    for a, i in endlocations.items():
        if all(grid[k[0]][k[1]] == a for k in i):
            continue
        if grid[i[0][0]][i[0][1]] == '.':
            loc = i[1]
            if grid[loc[0]][loc[1]] == a:
                continue
        else:
            loc = i[0]
        if grid[loc[0]][loc[1]] == '.':
            continue
        x = loc[1]
        for j in locations:
            if any(i>=x and i<=j[1] or i<=x and i>=j[1] for i in inarr):
                continue
            nd = energy + energyCalc(grid[loc[0]][loc[1]], loc, j)
            ngrid = [i.copy() for i in grid]
            ngrid[loc[0]][loc[1]] = '.'
            ngrid[j[0]][j[1]] = grid[loc[0]][loc[1]]
            ng = tuple(tuple(g) for g in ngrid)
            if ng not in dists or dists[ng] > nd:
                dists[ng] = nd
                heapq.heappush(arr, (nd, ng))
    for i in locations:
        if grid[i[0]][i[1]] == '.':
            continue
        res = endlocations[grid[i[0]][i[1]]]
        if grid[res[1][0]][res[1][1]] == '.':
            loc = res[1]
        else:
            loc = res[0]
        if any(k >= loc[1] and k < i[1] or k <= loc[1] and k > i[1] for k in inarr):
            continue
        nd = energy+energyCalc(grid[i[0]][i[1]], loc, i)
        ngrid = [i.copy() for i in grid]
        ngrid[i[0]][i[1]] = '.'
        ngrid[loc[0]][loc[1]] = grid[i[0]][i[1]]
        ng = tuple(tuple(g) for g in ngrid)
        if ng not in dists or dists[ng] > nd:
            dists[ng] = nd
            heapq.heappush(arr, (nd, ng))

print(dists[FINAL])
print(len(seen))