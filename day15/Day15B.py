import heapq

lines = [l.strip() for l in open("input.txt").readlines()]

arr = [[int(i) for i in line] for line in lines]

narr = [[(arr[(i%len(arr))][j%len(arr[0])] + (i//len(arr)) + (j//len(arr[0]))) for j in range(5*len(arr[0]))] for i in range(5*len(arr))]

for i in range(len(narr)):
    for j in range(len(narr[0])):
        narr[i][j]%=9
        if(narr[i][j] == 0):
            narr[i][j]+=9

arr=narr

states = [(0,0,0)]
heapq.heapify(states)

dists = [[100000000 for i in range(len(arr[0]))] for j in range(len(arr))]

dists[0][0] = 0

seen = [[False for i in range(len(arr[0]))] for j in range(len(arr))]

while states:
    s = heapq.heappop(states)
    i=s[1]
    j=s[2]
    if(seen[i][j]):
        continue
    seen[i][j] = True
    if i!=len(arr)-1:
       alt = dists[i][j]+arr[i+1][j]
       if alt < dists[i+1][j]:
            dists[i+1][j] = alt
            heapq.heappush(states, (alt, i+1, j))
    if j!=len(arr[0])-1:
        alt = dists[i][j] + arr[i][j+1]
        if alt < dists[i][j+1]:
            dists[i][j+1] = alt
            heapq.heappush(states, (alt, i, j+1))
    if i!=0:
       alt = dists[i][j]+arr[i-1][j]
       if alt < dists[i-1][j]:
            dists[i-1][j] = alt
            heapq.heappush(states, (alt, i-1, j))
    if j!=0:
        alt = dists[i][j] + arr[i][j-1]
        if alt < dists[i][j-1]:
            dists[i][j-1] = alt
            heapq.heappush(states, (alt, i, j-1))

print(dists[len(arr)-1][len(arr[0])-1])