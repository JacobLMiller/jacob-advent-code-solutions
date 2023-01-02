# Advent of code Year 2015 Day 5 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    input = [d.strip("\n") for d in input]

from itertools import pairwise
vowel_char = (
    "a", "e", "i", "o", "u"
)
def is_nice(s):
    double_letter = False
    vowels = 0
    for p1,p2 in pairwise(s):
        if p1+p2 in ["ab", "cd", "pq", "xy"]:
            return False 
        if p1 == p2:
            double_letter = True 
        if p1 in vowel_char:
            vowels += 1
    if s[-1] in vowel_char: vowels += 1

    if vowels >= 3 and double_letter: return True 
    return False
    
def is_nice_2(s):
    n = len(s)

    s_set = set()
    double = False
    space = False
    for i in range(n-1):
        s_p = s[i] + s[i+1]
        if s_p in s_set:
            if s_p[0] == s_p[1]:
                if s[i-1] != s_p[0]:
                # print(s_p)
                    double = True 
            else: double = True
        s_set.add(s_p)

        if i < n-2 and s[i] == s[i+2]:
            space = True 
    # print(f"double: {double}")
    # print(f"space: {space}")
    if space and double: 
        print(s)
    return space and double




count = 0 
p2 = 0
input = ["fkgrqbyqpqcworqc"]
for s in input:
    if is_nice(s): count += 1
    if is_nice_2(s): p2 += 1
print("Part One : "+ str(count))



print("Part Two : "+ str(p2))