# Advent of code Year 2017 Day 8 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]

regs = set()

ops = {
    ">": lambda x,y: x > y,
    "<": lambda x,y: x < y,
    "==": lambda x,y: x == y,
    "!=": lambda x,y: x != y,
    ">=": lambda x,y: x >= y,
    "<=": lambda x,y: x <= y
}

def parse_input(row):
    split = row.split(" ")
    reg, instr, size, _,reg2, op, val = split

    regs.add(reg)
    regs.add(reg2)

    if instr == "inc": size = int(size)
    elif instr == "dec": size = -int(size)

    ins = [ops[op], reg2, int(val), reg, size]
    
    return ins

instr = [parse_input(row) for row in input]

vals = {reg: 0 for reg in regs}

biggest = 0
for op, reg2, val, reg, size in instr:
    if op(vals[reg2],val):
        vals[reg] += size
        biggest = max(vals[reg],biggest)




print("Part One : "+ str(max(vals.values())))


print("Part Two : "+ str(biggest))