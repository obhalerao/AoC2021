lines = [l.strip() for l in open("input.txt").readlines()]
size = len(lines)
hz = 0
dep = 0
for i in range(size):
    lst = lines[i].split()
    amt = int(lst[1])
    if(lst[0] == "forward"):
        hz+=amt
    else:
        if(lst[0] == "down"):
            dep+=amt
        else:
            dep-=amt
print(hz*dep)