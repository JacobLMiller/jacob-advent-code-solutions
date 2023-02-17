# Advent of code Year 2016 Day 12 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]


instr = [d.split(" ") for d in input]

i = 0 

regs = {c: 0 for c in list("abcd")}

def sim(regs):
    i = 0
    while i < len(instr):
        ins = instr[i][0]
        if ins == "cpy":
            src, dest = instr[i][1:]
            if src.isnumeric():
                regs[dest] = int(src)
            else: regs[dest] = regs[src]
        elif ins == "inc":
            dst = instr[i][1]
            regs[dst] += 1
        elif ins == "dec":
            dst = instr[i][1]
            regs[dst] -= 1
        elif ins == "jnz":
            dst, jmp = instr[i][1:]
            val = regs[dst] if not dst.isnumeric() else int(dst)
            if val != 0:
                i = i + int(jmp)
                continue
        
        i += 1
    return regs['a']


start = {c: 0 for c in list("abcd")}
p1 = sim(start)

start['c'] = 1
p2 = sim(start)

print("Part One : "+ str(p1))



print("Part Two : "+ str(p2))