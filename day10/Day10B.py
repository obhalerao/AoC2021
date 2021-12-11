from collections import deque

lines = [l.strip() for l in open("input.txt").readlines()]

lefts = ['(','{','[', '<']
rights = [')','}', ']', '>']
points = {'(': 1, '{': 3, '[':2, '<': 4}
scores = []
for l in lines:
    stk = deque()
    s = 0
    bad = False
    for c in l:
        if c in lefts:
            stk.append(c)
        else:
            cur = stk.pop()
            if lefts.index(cur) != rights.index(c):
                bad = True
                break
    if(bad): continue
    while stk:
        s*=5
        cur=stk.pop()
        s+=points[cur]
    scores.append(s)

print(sorted(scores)[len(scores)//2])

