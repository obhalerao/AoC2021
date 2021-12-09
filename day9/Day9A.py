lines = [l.strip() for l in open("input.txt").readlines()]

arr = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        arr[i][j] = int(lines[i][j])

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        nbrs = []
        if(i != 0): nbrs.append(arr[i-1][j])
        if(i != len(arr)-1): nbrs.append(arr[i+1][j])
        if(j != 0): nbrs.append(arr[i][j-1])
        if(j != len(arr[0])-1): nbrs.append(arr[i][j+1])
        if(arr[i][j] < min(nbrs)): cnt+=(arr[i][j]+1)
print(cnt)