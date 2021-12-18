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

curSum = numbers[0]
for i in range(1, len(numbers)):
    curSum = add(curSum, numbers[i])
    while True:
        found = False
        for i in range(len(curSum)-1):
            if curSum[i][1] == curSum[i+1][1] and curSum[i][1] > 4:
                larr = curSum[:i]
                if len(larr) > 0:
                    larr[-1] = (larr[-1][0]+curSum[i][0], larr[-1][1])
                rarr = curSum[i+2:]
                if len(rarr) > 0:
                    rarr[0] = (rarr[0][0]+curSum[i+1][0], rarr[0][1])
                larr.append((0, curSum[i][1]-1))
                curSum = larr + rarr
                found = True
                break
        if found:
            continue
        for i in range(len(curSum)):
            if curSum[i][0] >= 10:
                a = curSum[i][0]//2
                b = curSum[i][0]-a
                larr = curSum[:i]
                rarr = curSum[i+1:]
                larr.append((a, curSum[i][1]+1))
                larr.append((b, curSum[i][1]+1))
                curSum = larr+rarr
                found = True
                break
        if not found:
            break
print(magnitude(curSum))