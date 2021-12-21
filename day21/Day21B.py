lines = [l.strip() for l in open("input.txt").readlines()]

p1 = int(lines[0].split(':')[1])
p2 = int(lines[1].split(':')[1])

s1=0
s2=0

die=0

p1t = True

cnt = 0

dp = [[[[[0 for i in range(2)] for j in range(10)] for k in range(10)] for m in range(40)] for n in range(40)]

dp[0][0][p1-1][p2-1][0] = 1

outcomes = [0,0,0,1,3,6,7,6,3,1]

for p1s in range(40):
    for p2s in range(40):
        if p1s >= 21 or p2s >= 21: continue
        for p1p in range(10):
            for p2p in range(10):
                for turn in range(2):
                    if(dp[p1s][p2s][p1p][p2p][turn] == 0): continue
                    oturn = 1-turn
                    for idx, s in enumerate(outcomes):
                        if turn == 0:
                            np1p = (p1p + idx) % 10
                            ns1 = p1s + (np1p+1)
                            if ns1 >= 40: continue
                            dp[ns1][p2s][np1p][p2p][oturn] += (s*dp[p1s][p2s][p1p][p2p][turn])
                        else:
                            np2p = (p2p + idx) % 10
                            ns2 = p2s + (np2p+1)
                            if ns2 >= 40: continue
                            dp[p1s][ns2][p1p][np2p][oturn] += (s*dp[p1s][p2s][p1p][p2p][turn])

a = sum(dp[i][j][k][l][m] for i in range(21, 40) for j in range(40) for k in range(10) for l in range(10) for m in range(2))
b = sum(dp[j][i][k][l][m] for i in range(21, 40) for j in range(40) for k in range(10) for l in range(10) for m in range(2))

print(a,b)
print(max(a,b))

