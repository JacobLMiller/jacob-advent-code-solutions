# Advent of code Year 2015 Day 23 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip().replace(",","") for d in input_file.readlines()]




def sim_regs(R):
    i = 0
    while i < len(input):
        instr = input[i].split()
        if instr[0] in ['jio', 'jie']:
            ins, reg, jmp = instr
            jmp = int(jmp[1:]) if jmp[0] == "+" else int(jmp)
            if ins == 'jio':
                if R[reg] == 1: 
                    i += jmp
                    continue
            if ins == 'jie':
                if R[reg] % 2 == 0:
                    i += jmp 
                    continue
            i += 1 
            continue 
        ins, reg = instr
        if ins == "jmp":
            jmp = int(reg[1:]) if reg[0] == "+" else int(reg)
            i += jmp
            continue

        if ins == "inc":
            R[reg] += 1
        elif ins == "tpl":
            R[reg] *= 3
        elif ins == "hlf":
            R[reg] //= 2
        
        i += 1
    return R['b']
    
p1 = sim_regs({'a': 0, 'b': 0})

print("Part One : "+ str(p1))

p2 = sim_regs({'a': 1, 'b': 0})

print("Part Two : "+ str(p2))