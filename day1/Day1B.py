lines = [l.strip() for l in open("input.txt").readlines()]
intlines = [int(i) for i in lines]
cnt=0
for i in range(len(intlines)-3):
    if(intlines[i]+intlines[i+1]+intlines[i+2] < intlines[i+1]+intlines[i+2]+intlines[i+3]): cnt+=1
print(cnt)