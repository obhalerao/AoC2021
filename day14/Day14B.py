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

cnts = {}
for i in range(len(lst)-1):
    st = lst[i]+lst[i+1]
    if st not in cnts:
        cnts[st] = 0
    cnts[st]+=1

print(cnts)

cnts2 = {}

for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    cnts2[i] = 0


for i in lst:
    cnts2[i] += 1

for itr in range(40):
    ncnts = {}
    for k,v in cnts.items():
        cur = k
        if cur in rules:
            cnts2[rules[cur]]+=v
            toAdd1 = k[0]+rules[cur]
            toAdd2 = rules[cur]+k[1]
            if cur not in ncnts:
                ncnts[cur]=0
            else:
                ncnts[cur]-=v
            if toAdd1 not in ncnts:
                if toAdd1 not in cnts:
                    ncnts[toAdd1]=0
                else:
                    ncnts[toAdd1]=cnts[toAdd1]
            ncnts[toAdd1]+=v
            if toAdd2 not in ncnts:
                if toAdd2 not in cnts:
                    ncnts[toAdd2]=0
                else:
                    ncnts[toAdd2]=cnts[toAdd2]
            ncnts[toAdd2]+=v
        else:
            ncnts[cur] = cnts[cur]

    cnts = ncnts


print(max(cnts2.values())-min(i for i in cnts2.values() if i > 0))


