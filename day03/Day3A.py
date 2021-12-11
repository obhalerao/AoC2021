lines = [l.strip() for l in open("input.txt").readlines()]

l = len(lines[0])

gamma = 0
epsilon = 0
for bit in range(l):
    zeros = 0
    for line in lines:
        if(line[bit] == '0'): zeros+=1
    ones = len(lines)-zeros
    if(ones > zeros):
        gamma+=1
    else:
        epsilon+=1
    gamma*=2
    epsilon*=2
print((gamma*epsilon)/4)