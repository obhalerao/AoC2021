lines = [l.strip('\n') for l in open("input.txt").readlines()]

grid = [[i for i in line] for line in lines]

cnt = 0

while True:
    moved = False
    ng = [['&' for i in line] for line in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '>':
                ni = i
                nj = (j+1)%len(grid[0])
                if grid[ni][nj] == '.':
                    moved = True
                    ng[i][j] = '.'
                    ng[ni][nj] = '>'
                else:
                    ng[i][j] = grid[i][j]
            elif ng[i][j] == '&':
                ng[i][j] = grid[i][j]
    grid = ng
    ng = [['&' for i in line] for line in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'v':
                ni = (i+1)%len(grid)
                nj = j
                if grid[ni][nj] == '.':
                    moved = True
                    ng[i][j] = '.'
                    ng[ni][nj] = 'v'
                else:
                    ng[i][j] = grid[i][j]
            elif ng[i][j] == '&':
                ng[i][j] = grid[i][j]
    grid = ng
    if moved:
        cnt+=1
    else:
        break
    print(grid[0])
print(cnt+1)
