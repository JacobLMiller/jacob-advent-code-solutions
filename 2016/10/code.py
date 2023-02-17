# Advent of code Year 2016 Day 10 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]


class Bot():
    def __init__(self,id,low_loc,high_loc):
        self.id = id 
        self.low = low_loc 
        self.high = high_loc

        self.chips = set()
    
    def give_chip(self,chip):
        self.chips.add(chip)
        assert len(self.chips) <= 2
    
    def compare(self):
        low,high = tuple(self.chips)
        if low > high: low,high = high,low 

        self.chips = set()
        return (low,self.low), (high,self.high)

class Output(Bot):
    def __init__(self,id):
        self.id = id 
        self.chips = set()


bots = dict()
# vals = [[int(d) for d in re.findall(r'\d+', line)] for line in input]
import re 
for line in input:
    if line[:3] == "bot":
        val = line.replace("bot ", '').replace(" gives low to ", ",").replace(" and high to ",",").replace("output ", "o")
        val = val.split(",")
        bots[val[0]] = Bot(*val)
        for v in val:
            if "o" in v:
                bots[v] = Output(v)

for line in input:
    if line[:3] == "val":
        val = re.findall(r'\d+', line)
        bots[val[1]].give_chip(int(val[0]))

cont = True
i = 0
while i < 1000:
    for bot in bots:
        if len(bots[bot].chips) == 2:
            (l_chip,l_dest),(h_chip,h_dest) = bots[bot].compare()

            if l_chip == 17 and h_chip == 61:
                p1 = bots[bot].id
            #     cont = False
            #     break

            bots[l_dest].give_chip(l_chip)
            bots[h_dest].give_chip(h_chip)
    i += 1




print("Part One : "+ str(p1))

p2 = [int(list(bots[d].chips)[0]) for d in ['o0','o1','o2']]

from math import prod
print("Part Two : "+ str(prod(p2)))