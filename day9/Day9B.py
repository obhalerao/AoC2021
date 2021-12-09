from collections import deque

lines = [l.strip() for l in open("input.txt").readlines()]

arr = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        arr[i][j] = int(lines[i][j])

lows = []
for i in range(len(arr)):
    for j in range(len(arr[0])):
        nbrs = []
        if(i != 0): nbrs.append(arr[i-1][j])
        if(i != len(arr)-1): nbrs.append(arr[i+1][j])
        if(j != 0): nbrs.append(arr[i][j-1])
        if(j != len(arr[0])-1): nbrs.append(arr[i][j+1])
        if(arr[i][j] < min(nbrs)): lows.append((i,j))

seen = set()
sizes = []
for pt in lows:
    if pt in seen: continue
    sz = 0
    q = deque()
    q.appendleft(pt)
    while q:
        cur = q.pop()
        if(arr[cur[0]][cur[1]] == 9): continue
        if cur in seen: continue
        seen.add(cur)
        sz+=1
        i = cur[0]
        j = cur[1]
        if (i != 0): q.appendleft((i-1, j))
        if (i != len(arr) - 1): q.appendleft((i+1, j))
        if (j != 0): q.appendleft((i, j-1))
        if (j != len(arr[0]) - 1): q.appendleft((i, j+1))
    sizes.append(sz)
sizes.sort()
print(sizes[-1]*sizes[-2]*sizes[-3])




