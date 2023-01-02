def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

import collections

def process_round(dirs, Elves):
    propose = dict()
    all_dir = dirs[0]+dirs[1]+dirs[2]+dirs[3]
    for E in Elves: 
        if all([E+d not in Elves for d in all_dir]): 
            propose[E] = E
            continue
        for dir in dirs:
            pot = [E + d for d in dir]
            if all([p not in Elves for p in pot]):
                propose[E] = E+dir[0]
                break
        else:
            propose[E] = E
    reverse = collections.defaultdict(list)
    for k,v in propose.items():
        reverse[v].append(k)
    
    for k,v in reverse.items():
        if len(v) > 1:
            for c in v:
                propose[c] = c 
    # print(len(set(propose.values())))
    new_elves = set(propose.values())
    return new_elves, new_elves == Elves

import random
def get_bounding_box(Elves):
    x1,x2,y1,y2 = 10000, -10000, 100000, -10000
    for p in Elves:
        x1 = min(x1, p.real)
        x2 = max(x2, p.real)
        y1 = min(y1, p.imag)
        y2 = max(y2, p.imag)
    return int(x1),int(x2),int(y1),int(y2)

def day23(data):
    Elves = set()
    h = len(data)
    w = len(data[0])
    for i in range(h):
        for j in range(w):
            if data[i][j] == "#": Elves.add(complex(j,h-i))

    north = [0+1j, -1+1j, 1+1j]
    south = [0-1j, -1-1j, 1-1j]
    east = [1, 1+1j, 1-1j]
    west = [-1, -1+1j, -1-1j]
    dirs = [north, south, west,east]
    uneql = False

    i = 1
    while not uneql:
        print(i)
        Elves, uneql = process_round(dirs,Elves)
        dirs = dirs[1:] + [dirs[0]]
        i += 1

    
    L,R,D,U = get_bounding_box(Elves)

    c = 0
    for i in range(L,R+1):
        for j in range(D,U+1):
            if complex(i,j) not in Elves:
                c += 1

    print(c)


if __name__ == "__main__":
    input = read_input("day23.txt")
    day23(input)

