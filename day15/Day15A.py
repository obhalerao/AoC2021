lines = [l.strip() for l in open("input.txt").readlines()]

arr = [[int(i) for i in line] for line in lines]

dp = [[100000000 for i in range(len(arr[0]))] for j in range(len(arr))]

dp[0][0] = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i != len(arr)-1:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+arr[i+1][j])
        if j != len(arr[0])-1:
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+arr[i][j+1])
print(dp[len(arr)-1][len(arr[0])-1])