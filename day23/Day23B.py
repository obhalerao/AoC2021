import heapq

lines = [l.strip('\n') for l in open("input.txt").readlines()]
INSERTION = ['  #D#C#B#A#', '  #D#B#A#C#']
lines.insert(3, INSERTION[1])
lines.insert(3, INSERTION[0])

grid = [[i for i in line] for line in lines[1:-1]]

locations = [(0,1),(0,2),(0,4),(0,6),(0,8),(0,10),(0,11)]

FINAL = '''#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#'''

STATE1 = '''#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#'''

STATE2 = '''#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#'''

STATE3 = '''#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#'''

STATE4 = '''#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#'''

STATE5 = '''#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#'''

STATE6 = '''#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#'''

STATE7 = '''#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#'''

STATE8 = '''#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#'''

STATE9 = '''#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#'''

STATE10 = '''#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#'''

STATE11 = '''#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#'''



FINAL = [list(i) for i in FINAL.split('\n')]
STATE1 = tuple(tuple(i) for i in STATE1.split('\n'))
STATE2 = tuple(tuple(i) for i in STATE2.split('\n'))
STATE3 = tuple(tuple(i) for i in STATE3.split('\n'))
STATE4 = tuple(tuple(i) for i in STATE4.split('\n'))
STATE5 = tuple(tuple(i) for i in STATE5.split('\n'))
STATE6 = tuple(tuple(i) for i in STATE6.split('\n'))
STATE7 = tuple(tuple(i) for i in STATE7.split('\n'))
STATE8 = tuple(tuple(i) for i in STATE8.split('\n'))
STATE9 = tuple(tuple(i) for i in STATE9.split('\n'))
STATE10 = tuple(tuple(i) for i in STATE10.split('\n'))
STATE11 = tuple(tuple(i) for i in STATE11.split('\n'))

endlocations = {'A':[(1,3),(2,3),(3,3),(4,3)],
                'B':[(1,5),(2,5),(3,5),(4,5)],
                'C':[(1,7),(2,7),(3,7),(4,7)],
                'D':[(1,9),(2,9),(3,9),(4,9)]}

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

def goodG(grid):
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
    c2 = sum(i.isalpha() for j in grid for i in j)
    if grid in seen:
        continue
    seen.add(grid)
    if len(seen) % 10000 == 0:
        print(len(seen))
    if grid == STATE9 or grid == STATE10 or grid == STATE11:
        print('hi')
    grid = [list(i) for i in grid]
    if(goodG(grid)):
        print('done')
        break
    inarr = []
    for j in locations:
        if grid[j[0]][j[1]] != '.':
            inarr.append(j[1])
    for a, i in endlocations.items():
        good = True
        for k in range(3):
            if not (grid[i[k][0]][i[k][1]] == '.' and grid[i[k+1][0]][i[k+1][1]] == a or grid[i[k][0]][i[k][1]] == a and grid[i[k+1][0]][i[k+1][1]] == a or grid[i[k][0]][i[k][1]] == '.' and grid[i[k+1][0]][i[k+1][1]] == '.'):
                good = False
                break
        if good:
            continue
        minidx = -1
        for k in range(4):
            if grid[i[k][0]][i[k][1]] != '.':
                minidx = k
                break
        loc = i[minidx]
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
            c = sum(i.isalpha() for j in ng for i in j)
            if c != 16:
                print('hmm')
            if ng not in dists or dists[ng] > nd:
                dists[ng] = nd
                heapq.heappush(arr, (nd, ng))
    for i in locations:
        if grid[i[0]][i[1]] == '.':
            continue
        res = endlocations[grid[i[0]][i[1]]]
        minidx = -2
        valid = True
        for k in range(4):
            if grid[res[k][0]][res[k][1]] != '.' and grid[res[k][0]][res[k][1]] != grid[i[0]][i[1]]:
                valid = False
                break
        if not valid:
            continue
        for k in range(4):
            if grid[res[k][0]][res[k][1]] != '.':
                minidx = k-1
                break
        if minidx == -1:
            continue
        if minidx == -2:
            minidx = 3
        loc = res[minidx]
        if any(k >= loc[1] and k < i[1] or k <= loc[1] and k > i[1] for k in inarr):
            continue
        nd = energy+energyCalc(grid[i[0]][i[1]], loc, i)
        ngrid = [i.copy() for i in grid]
        ngrid[i[0]][i[1]] = '.'
        ngrid[loc[0]][loc[1]] = grid[i[0]][i[1]]
        ng = tuple(tuple(g) for g in ngrid)
        c = sum(i.isalpha() for j in ng for i in j)
        if c != 16:
            print('hmm')
        if ng not in dists or dists[ng] > nd:
            dists[ng] = nd
            heapq.heappush(arr, (nd, ng))

print(dists[tuple(tuple(g) for g in FINAL)])

