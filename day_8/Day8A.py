lines = [l.strip() for l in open("input.txt").readlines()]
cnt=0
for l in lines:
    for idx, j in enumerate(l.split('|')):
        if(idx == 0): continue
        for k in j.strip().split():
            k = k.strip()
            if(len(k) == 2 or len(k) == 3 or len(k) == 7 or len(k) == 4):
                print(k)
                cnt+=1
print(cnt)