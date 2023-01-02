import numpy as np
from numba import jit

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

@jit(nopython=True)
def manhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def chug(data,size):
    sbdst = [manhattan(x1,y1,x2,y2) for x1,y1,x2,y2 in data]
    S = [(x1,y1) for x1,y1, _, __, in data]

    for y in range(size):
        span = list()
        for (x1,y1), dst in zip(S,sbdst):
            y_dist = y1 - y 
            if y_dist > dst: continue 
            span.append(( (x1 + abs(y_dist) - dst ), 
                        (x1 - abs(y_dist) + dst + 1)))

            span = sorted(span)
            print(span)
            max_col = 0
            print(zip(span[:-1], span[1:]))

            for (start1, stop1), (start2, stop2) in zip(span[:-1], span[1:]):
                if start2 > max_col and start2 > stop1 and (stop1, y ) not in S:
                    print(stop1, y)
                    return (stop1 * 400000 + y)
                else:
                    max_col = max(stop1, max_col)

@jit(nopython=True)
def get_dir(signs,num):
    iter = [[d] * num for d in signs]
    for elem in iter:
        for sign in elem:
            yield sign

@jit(nopython=True)
def tuple_add(p1,p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def chug2(S,size):
    signs = ( (1,1), (-1,1), (1,-1), (-1,-1) )
    B = (0,0)
    found = False



    for (x1,y1), dst in S.items():
        #Start at bottom of diamond
        x,y = x1, y1-(dst+1)
        #Use generator to save on space/time
        for dir in get_dir(signs, dst+1):

            if (0 <= x <= size) or (0 <= y <= size):
                for (x2,y2), dst2 in S.items():
                    #If current point dist is less than dst2 to other sensor, not valid 
                    if manhattan(x,y,x2,y2) <= dst2:
                        found = False
                        B = (0,0)
                        break 
                    else:
                        found = True
                        B = (x,y)
                if found:
                    return B[0] * 4000000 + B[1]
                    
            x,y = tuple_add((x,y), dir)
    



class Point():
    def __init__(self,x,y,t="N"):
        self.x = x 
        self.y = y
        self.t = t

class Grid():
    def __init__(self,h,w):
        self.h = h 
        self.w = w
        self.grid = dict()
        for i in range(h,w+1):
            for j in range(h,w+1):
                self.grid[(i,j)] = "U"


    def place(self,x,y,p):
        if self.grid[(x,y)] == "S" or self.grid[(x,y)] == "B": return
        self.grid[(x,y)] = p
    
    def fill_grid(self,S,x_off,y_off,dst):
        P1 = Point(S.x+x_off, S.y+y_off)
        P2 = Point(S.x - x_off, S.y - y_off)
        P3 = Point(S.x + x_off, S.y - y_off)
        P4 = Point(S.x - x_off, S.y + y_off)

        for P in (P1,P2,P3,P4):
            if manhattan(S,P) <= dst: self.place(P.x,P.y,"#")
    
    def count_known(self,y=10):
        c = 0
        mystr = ""
        for x in range(self.h,self.w+1):
            if self.grid[(x,y)] == "#": 
                c += 1
            mystr += self.grid[(x,y)]
        print(mystr)
        return c


def day15(data):
    data = [d.replace("Sensor at x=", "").replace(" y=", "").replace(": closest beacon is at x=",",").replace(" y=", "") for d in data]
    
    data = [ [int(x) for x in r.split(",")]
            for r in data]
    

    y = 10
    bound = 4000000

    pairs = list()
    beacons = set()
    not_poss = set()
    for x1,y1,x2,y2 in data:
        dst = manhattan(x1,y1,x2,y2) - abs(y1 - y)
        not_poss.update(range(x1 - dst, x1 + dst + 1))
        if y2 == y:
            not_poss.discard(x2)
    print(len(not_poss))

    S = {(x1,y1): manhattan(x1,y1,x2,y2) for x1,y1,x2,y2 in data}
    ans = chug2(S,bound)
    print(ans)
    # size = 400000
    # for y in range(size+1):
    #     not_poss = set() 
    #     print(f"On row {y}")
    #     for x1,y1,x2,y2 in data:
    #         dst = manhattan(x1,y1,x2,y2) - abs(y1 - y)
    #         up = list(range(x1-dst, x1+dst+1))
    #         up = [(x,y) for x in up if 0 <= x <= size]
    #         not_poss.update(up)
    #         # if y2 == y:
    #         #     not_poss.discard((x2,y2))
    #     if len(not_poss) == size:
    #         print("found it")
    #         got = sorted(list(not_poss))
    #         yt = got[0][1]
    #         for i,(x,yt) in enumerate(got):
    #             if i != x:
    #                 print((x-1)*4000000 + yt)
    #                 break
    #         break


    #abs(sy - y)
        
# for n in ns:
#     p1 = (n[0], n[1])
#     p2 = (n[2], n[3])
#     beacons.add(p2)
#     dist = manhattan(p1, p2)
#     for x in range(n[0] - dist, n[0] + dist + 1):
#         if manhattan(p1, (x, y)) <= dist:
#             cants.add((x, y))

if __name__ == "__main__":
    input = read_input('day15.txt')
    from time import perf_counter
    start = perf_counter()
    day15(input)
    print(f"Took a total of {perf_counter()-start}s for part 1 and 2")
