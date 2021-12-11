lines = [l.strip() for l in open("input.txt").readlines()]
cnt=0
for l in lines:
    vals = l.split('|')[0].strip().split()
    outs = l.split('|')[1].strip().split()
    stoi={}
    itos={}
    for i in vals:
        if(len(i) == 2):
            stoi[frozenset(i)] = 1
            itos[1] = frozenset(i)
        if(len(i) == 3):
            stoi[frozenset(i)] = 7
            itos[7] = frozenset(i)
        if(len(i) == 4):
            stoi[frozenset(i)] = 4
            itos[4]=  frozenset(i)
        if(len(i) == 7):
            stoi[frozenset(i)] = 8
            itos[8] = frozenset(i)
    arrmap = {}
    rem = list(itos[7] - itos[1])[0]
    arrmap[rem]='a'
    rem2=(itos[8] - itos[4] - {rem})
    for i in vals:
        if(rem2.intersection(frozenset(i)) != rem2 and len(rem2.intersection(frozenset(i))) == 1 and len(i) == 6):
            stoi[frozenset(i)] = 9
            itos[9] = frozenset(i)
    for i in vals:
        if(itos[9].intersection(frozenset(i)) == frozenset(i) and len(i) == 5):
            diff = itos[9]-frozenset(i)
            if(len(diff.intersection(itos[1])) > 0):
                stoi[frozenset(i)] = 5
                itos[5] = frozenset(i)
            else:
                stoi[frozenset(i)] = 3
                itos[3] = frozenset(i)
    diff2 = list(itos[4]-itos[5])[0]
    for i in vals:
        if(len({diff2}.intersection(i)) == 0 and len(i) == 6):
            stoi[frozenset(i)] = 6
            itos[6] = frozenset(i)
    for i in vals:
        if(frozenset(i) not in stoi and len(i) == 5):
            stoi[frozenset(i)] = 2
            itos[2] = frozenset(i)
        if(frozenset(i) not in stoi and len(i) == 6):
            stoi[frozenset(i)] = 0
            itos[0] = frozenset(i)
    cur=0
    for ou in outs:
        cur*=10
        cur+=(stoi[frozenset(ou)])
    print(cur)
    cnt+=cur

print(cnt)
