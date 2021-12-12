from collections import deque

lines = [l.strip() for l in open("input.txt").readlines()]

edges = {}

num_paths = {}



for line in lines:
    a = line.split('-')[0]
    b = line.split('-')[1]
    if a not in edges:
        edges[a] = []
    if b not in edges:
        edges[b] = []
    edges[a].append(b)
    edges[b].append(a)

paths = set()
stk = deque()
stk.append('start')

def process(stk):
    global paths, edges
    for e in edges[stk[-1]]:
        if e == 'end':
            stk.append(e)
            paths.add(tuple(stk.copy()))
            stk.pop()
        else:
            if e.isupper() or e not in stk:
                stk.append(e)
                process(stk)
                stk.pop()

process(stk)
print(len(paths))



