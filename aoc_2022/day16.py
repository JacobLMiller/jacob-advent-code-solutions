import numpy as np

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

def process(data):
    tmp = [
        d.replace("Valve ", "").replace("has flow rate=",",").replace("; tunnels lead to valves ",",").replace("; tunnel leads to valve", ",").replace(" ","").split(',')
        for d in data
    ]
    # print(tmp)
    return tmp


class Node():
    def __init__(self,name,fr,ind):
        self.name = name 
        self.neighbors = set()
        self.fr = fr
        self.opened = False if self.fr else True
        self.ind = ind

    def add_neighbor(self,v):
        self.neighbors.add(v)

    def get_neighbors(self):
        return self.neighbors

def BFS(nodes,s,t):

    Q = [s]
    explored = {s}
    dst = {s: 0}

    def visit_node(u,v):
        dst[u] = dst[v] + 1
        explored.add(u)
        Q.insert(0,u)

    while len(Q):
        v = Q.pop() 
        if v == t: break

        for u in v.get_neighbors():
            if u not in explored : 
                visit_node(u,v)

    return dst[t]



#dp[i][j][k] i=value at time i, j=current_pos, k=opened_valves



def day16(data):

    data = process(data)
    nodes = list()
    nm = dict()
    for i,row in enumerate(data):
        V = Node(row[0],int(row[1]), i)
        nodes.append(V)
        nm[row[0]] = i

    for i,row in enumerate(data):
        V = nodes[i]
        [V.add_neighbor(nodes[nm[u]]) for u in set(row[2:])]

    nonzero = [v for v in nodes if v.fr > 0 or v.name == "AA"]
    n = len(nonzero)
    D = np.zeros( (n,n),dtype=int)
    for i,u in enumerate(nonzero):
        for j,v in enumerate(nonzero):
            if i == j: continue 
            D[i,j] = BFS(nodes,u,v)
    nodes = nonzero
    nm = {v.name: v for i,v in enumerate(nodes)}
    FR = {i: v.fr for i,v in enumerate(nodes)}
    ind_map = {v.name: i for i,v in enumerate(nodes)}

    from functools import cache

    #Take the max over all possible destinations if the time to get there is less than time remaining, plus 
    #the time it would take to open the current valve
    @cache
    def recursive_dp(t, u, fr ):
        return max([FR[v] * (t-D[u,v]-1) + recursive_dp(t-D[u,v]-1, v, fr-{v})
           for v in fr if D[u,v]<t],default=0 ) 

    part1 = recursive_dp(30, ind_map["AA"], frozenset(FR))
    print(part1)
    

    @cache
    def elephant_dp(t, u, fr, elephant=False):
        return max([FR[v] * (t-D[u,v]-1) + elephant_dp(t-D[u,v]-1, v, fr-{v},elephant)
           for v in fr if D[u,v]<t] + [elephant_dp(26, u=ind_map["AA"], fr=fr) if elephant else 0],default=0 ) 
    

    part2 = elephant_dp(26, ind_map["AA"], frozenset(FR), True)
    print(part2)



if __name__ == "__main__":
    input = read_input("day16.txt")
    day16(input)