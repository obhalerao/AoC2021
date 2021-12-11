lines = [l.strip() for l in open("input.txt").readlines()]

l = len(lines[0])

oxygen = set(i for i in lines)
co2 = set(i for i in lines)
print(oxygen)

ox = True
co = True

for bit in range(l):
    ozeros = 0
    czeros = 0
    for line in lines:
        if(line[bit] == '0' and line in oxygen): ozeros+=1
        if (line[bit] == '0' and line in co2): czeros += 1
    oones = len(oxygen)-ozeros
    cones = len(co2)-czeros
    if ox:
        if oones >= ozeros:
            for i in lines:
                if(i[bit] == '0' and i in oxygen):
                    oxygen.remove(i)
        else:
            for i in lines:
                if(i[bit] == '1' and i in oxygen):
                    oxygen.remove(i)
    if co:
        if cones >= czeros:
            for i in lines:
                if(i[bit] == '1' and i in co2):
                    co2.remove(i)
        else:
            for i in lines:
                if(i[bit] == '0' and i in co2):
                    co2.remove(i)
    if len(oxygen) == 1:
        ox = False
    if len(co2) == 1:
        co = False
    print(oxygen,co2)

print(int(list(oxygen)[0], 2)*int(list(co2)[0], 2))
