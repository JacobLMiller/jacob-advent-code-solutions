def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

class Blizzard():
    def __init__(self,p,dir,w,h):
        self.p = p
        self.dir = dir
        self.w = w 
        self.h = h 
    
    def sim(self):
        newp = self.p + self.dir
        self.p = complex(newp.real % self.w, newp.imag % self.h)

def print_parents(parents, start):
    print(start)
    c = 0
    while start:
        print(parents[start])
        start = parents[start]
        if c > 18:
            break
        c += 1

def BFS(sims,s,d, wall,init_t):
    n = len(sims)

    Q = [(s, init_t)]
    explored = {(s, init_t)}
    dst = {(s,init_t): None}

    opt = {0,1,-1,1j,-1j}

    def visit_node(u,v):
        dst[u] = dst[v] + 1
        explored.add(u)
        Q.insert(0,u)

    while len(Q):
        v, t = Q.pop() 
        # print(t)
        if v == d:
            print_parents(dst, (v,t))
            return t

        for u in opt:
            newv = v + u 
            if (newv,t+1) not in explored and newv not in wall and newv not in sims[(t+1)%n]:
                dst[(newv,t+1)] = (v,t)
                explored.add((newv,t+1))
                Q.insert(0,(newv,t+1))


    return dst[t]



def day24(data):
    data = [d.replace("#", "") for d in data]
    h = len(data)
    w = len(data[0])

    dirmap = {
        "<": -1 + 0j, 
        ">": 1 + 0j, 
        "^": 0 - 1j,
        "v": 0 +1j
    }


    blizzards = list()
    check = data[1:len(data)-1]
    w = len(check[0])
    h = len(check)
    for i in range(w):
        for j in range(h):
            if check[j][i] in dirmap:
                blizzards.append( Blizzard(complex(i,j), dirmap[check[j][i]], w, h ))


    sims = list()
    for _ in range(1000):
        fs = set()
        for B in blizzards:
            fs.add(B.p)
            B.sim()
        if frozenset(fs) in sims:
            print("hey I've seen this before")
            break
        sims.append(frozenset(fs))
    
    tiles = set()
    for x in range(w):
        for y in range(h):
            tiles.add(complex(x,y))
    tiles.add(complex(0,-1))
    tiles.add(complex(w-1,h))


    sim_n = len(sims)

    dirs = {1, -1, 1j, -1j, 0}
    
    start = complex(0,-1)
    dest = complex(w-1,h)

    s_state = (start, sims[0], 0)
    Q = [s_state]

    depth = 0
    visited = set()
    parents = {s_state: None}

    walls = set()
    for i in range(-1,h+1):
        walls.add(complex(-1,i))
        walls.add(complex(w,i))
    for j in range(-1,w+1):
        walls.add(complex(j,-1))
        walls.add(complex(j,h))
    walls.add(complex(0,-2))
    walls.add(complex(w-1,h+1))
    walls.remove(start)
    walls.remove(dest)
    print(start)

    print(f"Part 1: {BFS(sims, start, dest, walls, 0)}")

    first = BFS(sims, start, dest, walls, 0)
    second = BFS(sims, dest, start, walls, first)
    print(f"Day 24 part 2: {BFS(sims, start, dest, walls, second)}")
    print()

        

    # while len(Q) > 0:
    #     loc, Bs, t = Q.pop()
    #     if loc == dest: 
    #         print_parents(parents, (loc, t%sim_n))
    #         print(f"shortest time is {t}")
    #         break
    

    #     # if t > depth:
    #     #     Q.sort(key=heuristic,reverse=False)
    #     #     Q = Q[:1000]
    #     #     depth += 1
        
    #     # if t > 18:
    #     #     break

    #     if (loc,t%sim_n) in visited: continue 
    #     visited.add((loc,t%sim_n))

    #     for d in dirs:
    #         newp = loc + d 
    #         if newp not in walls and newp not in Bs: 
    #             new_state = (newp, sims[(t+1)%sim_n], t+1)
    #             Q.insert(0, new_state)
    #             parents[(newp, (t+1)%sim_n)] = (loc,t%sim_n) 


    


if __name__ == "__main__":
    input = read_input("day24.txt")
    day24(input)