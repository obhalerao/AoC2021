lines = [l.strip() for l in open("input.txt").readlines()]

p1 = int(lines[0].split(':')[1])
p2 = int(lines[1].split(':')[1])

s1=0
s2=0

die=0

p1t = True

cnt = 0

while max(s1, s2) < 1000:
    s=0
    for i in range(3):
        s+=(die+1)
        die = (die+1)%100
    cnt+=3
    if p1t:
        p1 = (p1+s) % 10
        if p1 == 0:
            p1 = 10
        s1 += (p1)
    else:
        p2 = (p2+s) % 10
        if p2 == 0:
            p2 = 10
        s2 += (p2)
    p1t = not p1t
    print(s1, s2)

print(s1, s2)
print(min(s1, s2), cnt, min(s1, s2)*cnt)