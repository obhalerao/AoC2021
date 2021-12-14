from collections import Counter

lines = [l.strip() for l in open("input.txt").readlines()]

string = lines[0]

rules = {}
for idx in range(2, len(lines)):
    line = lines[idx].split(' -> ')
    strr = line[0]
    res = line[1]
    rules[strr] = res

lst = list(string)

for itr in range(40):
    nlst = []
    for i in range(len(lst)-1):
        cur = lst[i]+lst[i+1]
        toAdd = lst[i]
        if cur in rules:
            toAdd = lst[i]+rules[cur]
        for c in toAdd:
            nlst.append(c)
    nlst.append(lst[-1])
    lst = nlst



cnts = [0 for i in range(26)]
for i in lst:
    cnts[ord(i)-ord('A')]+=1
print(max(cnts)-min(i for i in cnts if i > 0))


