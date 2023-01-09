# Advent of code Year 2015 Day 7 solution
# Author = ?
# Date = December 2022

import numpy as np

test = """43690 -> d
21845 -> c
c AND d -> b
NOT b -> a"""

wires = dict()

def interpret(s):
    s = s.replace(" -> ", ",")
    op = None
    #lf AND lq,ls
    if "AND" in s:
        s = s.replace(" AND ", ",")
        op = "and"
    elif "OR" in s:
        s = s.replace(" OR ", ",")
        op = "or"
    elif "NOT" in s:
        s = s.replace("NOT ", "")
        op = "not"
    elif 'RSHIFT' in s:
        s = s.replace(" RSHIFT ", ",")
        op = 'rshift'
    elif "LSHIFT" in s:
        s = s.replace(" LSHIFT ", ",")
        op = 'lshift'
    else:
        op = 'assg'
    
    return op, s

def cr(val):
    n = 65536
    return ((val%n)+n)%n    

def get_not(x):
    bx = bin(x)[2:]
    bx = "0" * (16-len(bx)) + bx 
    newx = "".join("1" if c == "0" else "0" for c in bx)
    return int(newx,2)

def parseval(val):
    if val.isnumeric(): return int(val)
    else: return get_val(val)

def get_val(val):
    if not wires[val].val:
        wires[val].val = cr(wires[val].eval())
    return wires[val].val

class Wire():
    def __init__(self,op,s):
        self.eval = create(op,s)
        self.val = None

def create(op,s):
    if op == "and":
        s1,s2,dest = s.split(",")
        return lambda: parseval(s1) & parseval(s2)
    if op == "or":
        s1,s2,dest = s.split(",")
        return lambda: parseval(s1) | parseval(s2)
    elif op == "not":
        s1,dest = s.split(",")
        return lambda: ~ parseval(s1)
    elif op == "lshift":
        s1,s2,dest = s.split(",")
        return lambda: parseval(s1) << parseval(s2)
    elif op == "rshift":
        s1,s2,dest = s.split(",")
        return lambda: parseval(s1) >> parseval(s2)
    elif op == "assg":
        s1,dest = s.split(",")
        return lambda: parseval(s1)

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    input = [d.strip() for d in input]

# print(test.split("\n"))
# test = ["x AND y -> d"]
# input = test.split("\n")
def reset_wires(input):
    for line in input:
        op, s = interpret(line)
        dest = s.split(",")[-1]
        wires[dest] = Wire(op,s)

reset_wires(input)

ans = parseval('a')
print("Part One : "+ str(ans))

reset_wires(input)
wires['b'].val = ans 
ans2 = parseval('a')

print("Part Two : "+ str(ans2))