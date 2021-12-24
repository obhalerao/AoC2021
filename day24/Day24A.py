lines = [l.strip('\n') for l in open("input.txt").readlines()]



def execProg(input, z, lines):
    vars = [0,0,0,0]
    vars[3] = z
    idx = 0
    for line in lines:
        l = line.split()
        insn = l[0]
        if insn == 'inp':
            a = l[1]
            iadx = ord(a)-ord('w')
            vars[iadx] = int(input[idx])
            idx+=1
        else:
            a = l[1]
            b = l[2]
            a = ord(a)-ord('w')
            vara = vars[a]
            if b.isalpha():
                varb = vars[ord(b)-ord('w')]
            else:
                varb = int(b)
            if insn == 'add':
                vars[a] = vara+varb
            elif insn == 'mul':
                vars[a] = vara*varb
            elif insn == 'div':
                vars[a] = int(float(vara)/varb)
            elif insn == 'mod':
                vars[a] = vara%varb
            elif insn == 'eql':
                vars[a] = int(vara==varb)
    return vars
print(execProg(str(99911993949684), 0, lines))





