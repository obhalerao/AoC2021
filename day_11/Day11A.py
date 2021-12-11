from collections import deque

lines = [l.strip() for l in open("input.txt").readlines()]

arr = [[int(i) for i in l] for l in lines]

cnt = 0

for step in range(100):
    print(arr)
    q = deque()
    seen = set()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 9:
                q.append((i,j))
    while q:
        temp = q.popleft()
        if((temp[0], temp[1]) in seen): continue
        seen.add((temp[0], temp[1]))
        cnt+=1
        i = temp[0]
        j = temp[1]
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni = i+di
                nj = j+dj
                if ni < 0 or ni >= len(arr) or nj < 0 or nj >= len(arr[0]): continue
                if (ni, nj) in seen: continue
                arr[ni][nj] = min(arr[ni][nj]+1, 9)
                if(arr[ni][nj] == 9): q.append((ni, nj))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j] == 9):
                arr[i][j] = -1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j]+=1


    viewed = set()

print(cnt)
