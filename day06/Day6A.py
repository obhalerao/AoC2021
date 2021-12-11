lines = [l.strip() for l in open("input.txt").readlines()]

fish = [int(i) for i in lines[0].split(',')]

for day in range(256):
    l = len(fish)
    for j in range(l):
        if(fish[j] == 0):
            fish.append(8)
            fish[j] = 6
        else:
            fish[j]-=1


print(len(fish))
