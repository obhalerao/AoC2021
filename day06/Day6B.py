lines = [l.strip() for l in open("input.txt").readlines()]

fish = [int(i) for i in lines[0].split(',')]
cnts = [0 for i in range(9)]

for f in fish:
    cnts[f]+=1

for day in range(256):
    l = len(fish)
    ncnts = [0 for i in range(9)]
    for j in range(len(cnts)):
        if(j == 0):
            ncnts[6]+=cnts[j]
            ncnts[8]+=cnts[j]
        else:
            ncnts[j-1]+=cnts[j]
    cnts = ncnts


print(sum(cnts))
