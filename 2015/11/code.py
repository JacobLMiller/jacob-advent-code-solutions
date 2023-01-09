# Advent of code Year 2015 Day 11 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


str_map = dict(zip(
    list("abcdefghijklmnopqrstuvwxyz"),
    range(26)
))

num_map = dict(zip(
    range(26),
    list("abcdefghijklmnopqrstuvwxyz")
))

bad = {str_map[c] for c in ['i', 'o', 'l']}

# input = "abcdefgh"

s = [str_map[c] for c in input]

def is_valid(s):
    s_set = dict()
    has_increasing = False
    doubles = 0
    for i,val in enumerate(s):
        if val in bad:
            return False 
        if i < len(s)-2 and s[i+1] == val+1 and s[i+2] == val+2:
            has_increasing = True
        if i < len(s)-1 and val == s[i+1]:
            s_p = val
            if s_p in s_set:
                if s_set[s_p] != i: doubles += 1 
            else: 
                s_set[s_p] = i+1
                doubles += 1
        # if doubles and has_increasing: return True 
    return doubles >= 2 and has_increasing

def increment(s):
    n = len(s)
    for i in range(-1,-n-1,-1):
        s[i] += 1
        if s[i] < 26: break 
        s[i] = 0
    
    return s
        
while not is_valid(s):
    s = increment(s)

print("Part One : "+ str("".join(num_map[c] for c in s)))

s = increment(s)
while not is_valid(s):
    s = increment(s)

print("Part Two : "+ str("".join(num_map[c] for c in s)))