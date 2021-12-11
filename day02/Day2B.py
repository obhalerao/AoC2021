lines = [l.strip() for l in open("input.txt").readlines()]
size = len(lines)
hz = 0
dep = 0
aim = 0
for i in range(size):
    lst = lines[i].split()
    amt = int(lst[1])
    if(lst[0] == "forward"):
        hz+=amt
        dep+=(aim*amt)
    else:
        if(lst[0] == "down"):
            aim+=amt
        else:
            aim-=amt
print(hz*dep)