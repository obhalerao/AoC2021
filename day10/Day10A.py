from collections import deque

lines = [l.strip() for l in open("input.txt").readlines()]

lefts = ['(','{','[', '<']
rights = [')','}', ']', '>']
points = {')': 3, '}': 1197, ']':57, '>': 25137}
s=0
for l in lines:
    stk = deque()
    for c in l:
        if c in lefts:
            stk.append(c)
        else:
            cur = stk.pop()
            if lefts.index(cur) != rights.index(c):
                s+=points[c]
                break
print(s)

