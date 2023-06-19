# Advent of code Year 2016 Day 23 solution
# Author = ?
# Date = December 2022

def get_input():
    with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
        input = [d.strip().split(" ") for d in input_file.readlines()]
    return input

def reduce_input(inp):
    for i in range(len(inp)):
        if inp[i][0] == "cpy" and inp[i+1][0] == "inc" and inp[i+2][0] == "dec":
            print("hello")
            if inp[i+3][0] == "jnz" and inp[i+4][0] == "dec" and inp[i+5][0] == "jnz":
                inp[i] = ["peep"]
                for j in range(5):
                    inp[i+j+1] = ["noop"]

    return inp

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

def check_output(out):
    if out == [0 if i % 2 == 0 else 1 for i in range(len(out))]:
        return True 
    elif out == [1 if i % 2 == 0 else 0 for i in range(len(out))]:
        return True 
    else:
        return False

def sim(instr,regs):
    i = 0
    output = []
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
            regs['d'] += (633*regs['c'])
            regs['c'] = 0 
            regs['b'] = 0
        elif ins == "out":
            _,val = instr[i]
            val = parse_int(val,regs)
            output.append(val)
            if len(output) > 500:
                return check_output(output)
        elif ins == "noop":
            pass
        
        i += 1
    return regs['a']

regs = {c: 0 for c in list("abcd")}
regs['a'] = 0

input = get_input()

input = reduce_input(input)

print(input)

for i in range(1000):
    regs = {c: 0 for c in list("abcd")}
    regs['a'] = i
    print(f"On trial {i}")
    p1 = sim(input,regs)
    if p1: 
        p1 = i
        break


print("Part One : "+ str(p1))


print("Part Two : "+ str(None))