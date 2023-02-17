# Advent of code Year 2016 Day 18 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
# input = ".^^.^.^^^^"

def is_trap(l,c,r):
    if not l and not c and r: return True 
    elif l and not c and not r: return True
    elif not l and c and r: return True 
    elif l and c and not r: return True
    else: return False 

def get_tile(row,left,center,right):
    l = True if left < 0 or row[left] == "." else False
    c = True if row[center] == "." else False 
    r = True if right >= len(row) or row[right] == "." else False

    if is_trap(l,c,r): return "^"
    else: return "."

def new_row(row):
    return "".join(get_tile(row,i-1,i,i+1) for i in range(len(row)))


import tqdm
def total_safe(input,n=40):
    old = input
    count_safe = lambda s: sum(True if c == "." else False for c in s)
    p1 = count_safe(old)
    for i in tqdm.tqdm(range(n-1)):
        old = new_row(old)
        p1 += count_safe(old)
    return p1


p1 = total_safe(input,40)
print("Part One : "+ str(p1))


p2 = total_safe(input,400000)
print("Part Two : "+ str(p2))