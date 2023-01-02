import numpy as np
from itertools import cycle
from tqdm import tqdm

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

rightbound = 8
leftbound = 0

impassable = ["sand", "rock"]

####
shapes = [
    [3 + 0j, 4+0j, 5+0j, 6+0j], #horiz line
    [4 + 0j, 3 + 1j, 4 + 1j, 5 + 1j, 4 + 2j], #Plus sign
    [3 + 0j, 4 + 0j, 5 + 0j, 5 + 1j, 5 + 2j], #Backwards L 
    [3 + 0j, 3 + 1j, 3 + 2j, 3 + 3j], #Vert line 
    [3 + 0j, 4 + 0j, 3 + 1j, 4 + 1j] #Block
]

class Rock():
    def __init__(self,points):
        self.points = points
        self.falling = True
        

    def can_push(self,dir,universe):
        for p in self.points:
            if p + dir in universe or not leftbound < p.real + dir < rightbound:
                return False 
        return True
    
    def can_fall(self,universe):
        for p in self.points:
            if p - 1j in universe: 
                return False 
        return True

    def fall(self,dir,universe):
        if self.can_push(dir,universe):
            self.points = [p + dir for p in self.points]
        if self.can_fall(universe):
            self.points = [p - 1j for p in self.points]
        else: 
            self.falling = False
    
    def get_heights(self):
        p = self.points + [0]




def get_rock(r,top):
    return Rock([x + complex(0,top) for x in shapes[r]])

def day17(data,num):
    jets = data[0]
    jets = [-1 if j == "<" else 1 for j in jets]
    num_jets = len(jets)
    j_count = 0
    j = cycle(jets)

    rock_count = 0
    jet_count = 0
    i = 0

    top = 0
    universe = set([x + 0j for x in range(1,8)])

    old_c = 0
    deltas = list()
    for i in tqdm(range(num)):

        R = get_rock(rock_count, top+4)
        while R.falling: 
            J = jets[jet_count]
            jet_count = (jet_count + 1) % num_jets
            R.fall(next(j),universe)
        
        universe.update(R.points)
        top = max(top, max([int(y.imag) for y in R.points]))

        rock_count = (rock_count + 1) % 5

        deltas.append(top-old_c)
        old_c = top
        

        


    print(f"The tower is {int(top)} units tall")
    return deltas

def find_cycle(deltas):
    for i in range(len(deltas)):
        sl = deltas[i:]
        for j in range(2, len(sl) // 2):
            if sl[:j] == sl[j:2*j]:
                if all([(sl[:j] == sl[k:k+j]) for k in range(j, len(sl) - j, j)]):
                    return deltas[:i], deltas[i:i+j]


if __name__ == "__main__":
    input = read_input("day17.txt")
    day17(input,2022)
    deltas = day17(input, 10000)
    prefix, cyc = find_cycle(deltas)
    print(prefix)

    len_p, len_c = len(prefix), len(cyc)
    n = 1000000000000

    p2 = sum(prefix) + sum(cyc) * ((n-len_p) // len_c) + sum(cyc[:((n - len_p) % len_c)])
    print(f"The tower is {p2} units tall after {n} iterations")

    # day17(input, 1000000000000)