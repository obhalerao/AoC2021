lines = [l.strip() for l in open("input.txt").readlines()]
intlines = [int(i) for i in lines]
cnt=0
for i in range(len(intlines)-1):
    if(intlines[i] < intlines[i+1]): cnt+=1
print(cnt)