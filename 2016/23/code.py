# Advent of code Year 2016 Day 23 solution
# Author = ?
# Date = December 2022

def get_input():
    with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
        input = [d.strip().split(" ") for d in input_file.readlines()]
    return input

def toggle(instr):
    if len(instr) == 2:
        ins, dst = instr 
        if ins == "inc": return ["dec", dst]
        else: return ["inc", dst]
    elif len(instr) == 3:
        ins,d1,d2 = instr 
        if ins == "jnz": return ["cpy", d1,d2]
        else: return ["jnz", d1, d2]

def parse_int(n,regs):
    try: 
        val = int(n)
    except ValueError:
        val = regs[n]
    return val


def sim(instr,regs):
    i = 0
    while i < len(instr):
        ins = instr[i][0]
        if ins == "cpy":
            src, dest = instr[i][1:]
            src = parse_int(src,regs)
            regs[dest] = src
        elif ins == "inc":
            dst = instr[i][1]
            regs[dst] += 1
        elif ins == "dec":
            dst = instr[i][1]
            regs[dst] -= 1
        elif ins == "jnz":
            dst, jmp = instr[i][1:]
            val = parse_int(dst,regs)
            jmp = parse_int(jmp,regs)
            if val != 0:
                i = i + int(jmp)
                continue
        elif ins == "tgl":
            dst = instr[i][1]
            val = parse_int(dst,regs)
            if 0 <= val + i < len(instr):
                instr[val+i] = toggle(instr[val+i])
        elif ins == "peep":
            regs['a'] += (regs['b']*regs['d'])
            regs['c'] = 0 
            regs['d'] = 0
        elif ins == "noop":
            pass
        
        i += 1
    return regs['a']

regs = {c: 0 for c in list("abcd")}
regs['a'] = 7

input = get_input()

p1 = sim(input,regs)


print("Part One : "+ str(p1))

input = get_input()
regs = {c: 0 for c in list("abcd")}
regs['a'] = 12


input = input[:4] + [["peep"]] + [["noop"]]*5 + input[10:]
p2 = sim(input,regs)

print("Part Two : "+ str(p2))