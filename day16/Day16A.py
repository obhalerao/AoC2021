lines = [l.strip() for l in open("input.txt").readlines()]

st = lines[0]

versionTotal = 0

def parsePacket(enc):
    global versionTotal
    numParsed = 0
    version = int(enc[:3], 2)
    versionTotal+=version
    enc = enc[3:]
    numParsed+=3
    typeid = int(enc[:3], 2)
    enc = enc[3:]
    numParsed+=3
    if typeid == 4:
        curStr = ''
        while True:
            currGroup = enc[:5]
            enc = enc[5:]
            numParsed+=5
            curStr+=currGroup[1:]
            if(currGroup[0] == '0'):
                break
        return enc, numParsed
    else:
        ltid = enc[0]
        enc = enc[1:]
        numParsed+=1
        if(ltid == '0'):
            nbits = int(enc[:15], 2)
            enc = enc[15:]
            numParsed+=15
            while nbits > 0:
                cur, numParsed2 = parsePacket(enc)
                nbits-=numParsed2
                enc = cur
                numParsed+=numParsed2
        else:
            npackets = int(enc[:11], 2)
            enc = enc[11:]
            numParsed+=11
            for i in range(npackets):
                cur, numParsed2 = parsePacket(enc)
                enc = cur
                numParsed+=numParsed2
        return enc, numParsed


enc = ''
for i in st:
    cur = bin(int(i, 16))[2:]
    while len(cur) < 4:
        cur = '0'+cur
    enc+=cur

parsePacket(enc)
print(versionTotal)


