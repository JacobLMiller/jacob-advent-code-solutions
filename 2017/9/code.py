# Advent of code Year 2017 Day 9 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# input = "{{<a!>},{<a!>},{<a!>},{<ab>}}"

import re

def remove_substring(s):
    ns = ""
    i = 0 
    while i < len(s):
        if s[i] == "!" and i < len(s)-1:
            i += 2 
        else:
            ns += s[i]
            i += 1
    return ns

def remove_between_angle_brackets(string):
    pattern = r"<.*?>"
    return re.sub(pattern, "", string)    

ns = remove_substring(input)
og_len = len(ns)

ns = remove_between_angle_brackets(ns)

depth = 0 
p1 = 0
for c in ns:
    if c == "{":
        depth += 1
    elif c == "}":
        p1 += depth 
        depth -= 1


print("Part One : "+ str(p1))

nns = remove_substring(input)
pattern = r"<.*?>"
nns = re.sub(pattern,"!",nns)

num_brackets = nns.count("!")
p2 = og_len - len(ns) - 2*num_brackets

print("Part Two : "+ str(p2))