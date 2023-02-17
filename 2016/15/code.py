# Advent of code Year 2016 Day 15 solution
# Author = ?
# Date = December 2022

import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]

class Disc:
    def __init__(self,num_pos,cur_pos):
        self.num_pos = num_pos
        self.cur_pos = cur_pos

    def turn(self,num):
        self.cur_pos = (self.cur_pos + num) % self.num_pos
        return self.cur_pos == 0

def parse_discs():
    discs = list()
    for line in input:
        _,num_pos,__,cur_pos = re.findall(r'\d+',line)
        discs.append((int(num_pos), int(cur_pos)))
    return discs

def drop(discs,start=0):

    for i, (mod,pos) in enumerate(discs,1):
        if (pos+i+start) % mod != 0:
            return False 
    else: return True


discs = parse_discs()
i = 0
while True:
    if i % 10000 == 0: print(i)
    if drop(discs,start=i):
        p1 = i 
        break
    i += 1

discs = parse_discs()
discs += [(11,0)]
i = 0 
while True:
    if i % 10000 == 0: print(i)
    if drop(discs,start=i):
        p2 = i 
        break
    i += 1

    

print("Part One : "+ str(p1))



print("Part Two : "+ str(p2))