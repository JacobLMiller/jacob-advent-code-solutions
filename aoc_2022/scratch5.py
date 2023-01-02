import numpy as np

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

types = ["air", "rock", "sand"]

impassable = ["rock", "sand"]


class Point():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.type = "air"
        self.rest = 0
    
    def set_type(self,type):
        if type not in types: return
        self.type = type

class Sand(Point):

    def fall(self,D):

        x,y = self.x, self.y 
        if (x,y+1) in D and D[(x,y+1)] in impassable:
                #Check down and left
            if (x-1,y+1) in D and D[(x-1,y+1)] in impassable:
                ##Check down and right
                if (x+1, y+1) in D and D[(x+1,y+1)] in impassable:
                    ##Rest 
                    self.set_rest()
                else:
                    #move down and right
                    self.update(x+1,y+1,D)
            else:
                #Move down and left
                self.update(x-1,y+1,D)
        else:
            #Move down
            self.update(x,y+1,D)

    def update(self,newx,newy,D):
        D[(self.x,self.y)] = "air"
        self.x,self.y = newx, newy
        D[(newx,newy)] = "sand"

    def set_rest(self):
        self.rest = 1



class Line():
    def __init__(self,p1,p2):
        self.p1 = p1 
        self.p2 = p2 
        self.horiz = True if self.p1.y == self.p2.y else False
    
    def fill_dict(self,D):
        start, stop = (self.p1.x, self.p2.x) if self.horiz else (self.p1.y, self.p2.y)
        L = [ x for x in range(min(start,stop),max(start,stop)+1) ]
        for p in L:
            add_p = (p,self.p1.y) if self.horiz else (self.p1.x, p)
            D[add_p] = "rock"




def challenge14(data):
    data = [d.strip().replace(" ", "").split("->") for d in data]
    lines = list()

    minx,maxx,miny,maxy = 10000, -10000, 10000, -10000
    for row in data:
        lines.append(list())
        for i in range(len(row)-1):
            (x1,y1), (x2,y2) = row[i].split(","), row[i+1].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            p1 = Point(int(x1), int(y1))
            p2 = Point(int(x2), int(y2))
            L = Line(p1,p2)
            lines[-1].append(L)
            minx,maxx,miny, maxy = min(minx, x1, x2),max(maxx,x1,x2), min(miny, y1, y2), max(maxy,y1,y2)
    

    D = dict()
    for poly in lines:
        [L.fill_dict(D) for L in poly]
    for x in range(minx,maxx+1):
        for y in range(0,maxy):
            if (x,y) not in D:
                D[(x,y)] = 'air'
    
    sand_falling = True
    sands = 0
    while(sand_falling):
        s = Sand(500,0)
        sands += 1
        while(not s.rest):
            s.fall(D)
            # print((s.x,s.y))
            if s.y >= maxy:
                sand_falling = False 
                break
    print(f"Day 14 part 1: {sands}")

    #part 2
    import time 
    start = time.perf_counter()
    D = dict()
    for poly in lines:
        [L.fill_dict(D) for L in poly]
    for x in range(minx,maxx+1):
        for y in range(0,maxy):
            if (x,y) not in D:
                D[(x,y)] = 'air'
    
    for x in range(-10000,10000):
        D[(x,maxy+2)] = "rock"

        
    sands = 0
    while(True):
        s = Sand(500,0)
        sands += 1
        while(not s.rest):
            s.fall(D)
        if (s.x,s.y) == (500,0):
            break

    end = time.perf_counter()
    print(f"Day 14 part 2: {sands}")
    print(f"Took {end-start} seconds")

if __name__ == "__main__":
    data = read_input('day14.txt')
    challenge14(data)
