lines = [l.strip() for l in open("input.txt").readlines()]

enhance = lines[0]

image = []
for line in lines[2:]:
    image.append([i for i in line])

positive = False

for iter in range(50):
    enhanced = [['.' for i in range(len(image[0])+2)] for j in range(len(image)+2)]
    for x in range(len(enhanced)):
        for y in range(len(enhanced[0])):
            num = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    num *= 2
                    nx,ny = x+dx-1,y+dy-1
                    if nx < 0 or nx >= len(image) or ny < 0 or ny >= len(image[0]):
                        if positive: num+=1
                        continue
                    if image[nx][ny] == '#':
                        num+=1

            enhanced[x][y] = enhance[num]
    image = enhanced
    if positive:
        positive = (enhance[511] == '#')
    else:
        positive = (enhance[0] == '#')

print(len(image))
print(positive)

print(sum(i.count('#') for i in image))