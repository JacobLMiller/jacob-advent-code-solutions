# Advent of code Year 2015 Day 2 solution
# Author = ?
# Date = December 2022

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    input = [l.strip("\n").replace("x", ",").split(",") for l  in input]
    input = [[int(d) for d in l] for l in input]

# 2*l*w + 2*w*h + 2*h*l + min(w,l,h)
#test = 2x3x4
p1 = 0
for l,w,h in input:
    p1 += ( (2*l*w) + (2*w*h) + (2*h*l) + min(l*w,w*h,h*l) )

print("Part One : "+ str(p1))

p2 = 0
for l,w,h in input:
    m1,m2 = sorted([l,w,h])[0:2]
    p2 += ( (m1+m1) + (m2+m2) ) + (l*w*h)

print("Part Two : "+ str(p2))