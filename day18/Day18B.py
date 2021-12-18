lines = [l.strip() for l in open("input.txt").readlines()]

numbers = []

for line in lines:
    level = 0
    num = []
    for c in line:
        if c == '[':
            level+=1
        elif c == ']':
            level-=1
        elif c.isdigit():
            num.append((int(c), level))
    numbers.append(num)

def add(num1, num2):
    result = num1+num2
    for i in range(len(result)):
        result[i] = (result[i][0], result[i][1]+1)
    return result

def magnitude(num):
    stk = []
    for i in range(len(num)):
        cur = num[i]
        while stk and cur[1] == stk[-1][1]:
            rgt = stk.pop()
            sm = 3*rgt[0] + 2*cur[0]
            cur = (sm, cur[1]-1)
        stk.append(cur)
    return stk[0][0]

maxMag = 0

for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if i == j: continue
        curSum = add(numbers[i], numbers[j])
        while True:
            found = False
            for ii in range(len(curSum)-1):
                if curSum[ii][1] == curSum[ii+1][1] and curSum[ii][1] > 4:
                    larr = curSum[:ii]
                    if len(larr) > 0:
                        larr[-1] = (larr[-1][0]+curSum[ii][0], larr[-1][1])
                    rarr = curSum[ii+2:]
                    if len(rarr) > 0:
                        rarr[0] = (rarr[0][0]+curSum[ii+1][0], rarr[0][1])
                    larr.append((0, curSum[ii][1]-1))
                    curSum = larr + rarr
                    found = True
                    break
            if found:
                continue
            for ii in range(len(curSum)):
                if curSum[ii][0] >= 10:
                    a = curSum[ii][0]//2
                    b = curSum[ii][0]-a
                    larr = curSum[:ii]
                    rarr = curSum[ii+1:]
                    larr.append((a, curSum[ii][1]+1))
                    larr.append((b, curSum[ii][1]+1))
                    curSum = larr+rarr
                    found = True
                    break
            if not found:
                break
        maxMag = max(maxMag, magnitude(curSum))
print(maxMag)