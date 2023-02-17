# Advent of code Year 2016 Day 9 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

s = input
def decompress(s):
    p1 = ""

    i = 0
    while i < len(s):
        if s[i] == "(":
            ind = s[i:].find(")") + i
            sp = s[i+1:ind]
            sp = sp.split("x")
            num, rep = sp 
            num, rep = int(num), int(rep)

            p1 += "".join([ s[ind+1 : ind+1+num] ] * rep)

            i = ind + num + 1
        else:
            p1 += s[i]
            i += 1
    return p1

p1 = decompress(input)

print("Part One : "+ str(len(p1)))

s,i,p2 = input, 0, 0
w = [1 for _ in range(len(s))]

while i < len(s):
    if s[i] == "(":
        ind = s[i:].find(")") + i 
        sp = s[i+1:ind]
        sp = sp.split("x")
        num, rep = int(sp[0]), int(sp[1])

        for j in range(num):
            w[ind+1+j] *= rep
        
        i = ind+1

    else:
        p2 += w[i]
        i += 1


print("Part Two : "+ str(p2))