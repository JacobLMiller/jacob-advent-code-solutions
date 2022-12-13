import numpy as np 
# import networkx as nx

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

####THIS IS GARBAGE
# def challenge12(data):
#     map = dict( 
#         zip(list("abcdefghijklmnopqrstuvwxyz"),
#         [i for i in range(0,26)])
#     )
#     n = len(data)

#     data = [list(d) for d in data]
#     G = nx.DiGraph()
#     nodes = [(i,j) for j in range(n) for i in range(n)]
    
#     G.add_nodes_from(nodes)

#     heightmap = [[0 for _ in d] for d in data]

#     start_node = None
#     end_node = None
#     for i, row in enumerate(data):
#         for j, char in enumerate(row):
#             if char == "S":
#                 heightmap[i][j] = map['a']
#                 start_node = (i,j) 
#             elif char == "E":
#                 heightmap[i][j] = map['z']
#                 end_node = (i,j)
#             else:
#                 heightmap[i][j] = map[char]

#     n_rows = len(data)
#     n_col = len(data[0])
#     for i,row in enumerate(data):
#         for j, height in enumerate(row):
#             if i == j: continue
#             cur_h = heightmap[i][j]
#             #check left
#             if j > 0 and cur_h >= heightmap[i][j-1]-1 :
#                 G.add_edge((i,j), (i,j-1))
#             if j < n_col-1 and cur_h >= heightmap[i][j+1]-1:  
#                 G.add_edge((i,j), (i,j+1))
#             if i > 0 and  cur_h >= heightmap[i-1][j]-1:
#                 G.add_edge((i,j), (i-1,j))
#             if i < n_rows-1 and cur_h >= heightmap[i+1][j]-1:
#                 G.add_edge((i,j), (i+1,j))

#     print(nx.shortest_path_length(G, start_node,end_node))
#     A = (20,89)
#     B = (20,88)
#     print(G.has_edge(A,B))
#     # print(heightmap[20][5])
#     # print(heightmap[20][4])


def BFS(s,t, heightmap):
    nrow = len(heightmap)
    ncol = len(heightmap[0])

    Q = [s]
    explored = {s}
    dst = {s: 0}

    def visit_node(u,v):
        dst[u] = dst[v] + 1
        explored.add(u)
        Q.insert(0,u)

    while len(Q):
        v = Q.pop()
        if v == t:
            break 

        i,j = v 
        #Look up
        h = heightmap[i][j]
        if i > 0 and heightmap[i-1][j] - 1 <= h:
            u = (i-1,j)
            if u not in explored: visit_node(u,v)
        #Look down
        if i < nrow-1 and heightmap[i+1][j] - 1 <= h:
            u = (i+1,j)
            if u not in explored: visit_node(u,v)
        #Look left
        if j > 0 and heightmap[i][j-1] - 1 <= h:
            u = (i,j-1)
            if u not in explored: visit_node(u,v)
        #Look right
        if j < ncol-1 and heightmap[i][j+1] - 1 <= h:
            u = (i,j+1)
            if u not in explored: visit_node(u,v)

    return dst[t] if t in dst else 1e100

def challenge12_new(data):
    map = dict( zip(
        list("abcdefghijklmnopqrstuvwxyz"),
        [i for i in range(0,26)]
    ))

    data = [list(d) for d in data]

    nrow = len(data)
    ncol = len(data[0])
    
    heightmap = [[0 for _ in d] for d in data]

    start_node = None
    end_node = None
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "S":
                heightmap[i][j] = map['a']
                start_node = (i,j) 
            elif char == "E":
                heightmap[i][j] = map['z']
                end_node = (i,j)
            else:
                heightmap[i][j] = map[char]
    

    
    dst = BFS(start_node,end_node,heightmap)
    print(dst)

    #Part 2
    a_locs = list()
    for i,row in enumerate(heightmap):
        for j, h in enumerate(row):
            if h == map['a']: a_locs.append((i,j))

    dst = min([BFS(a,end_node,heightmap) for a in a_locs])
    print(dst)

        


if __name__ == "__main__":
    input = read_input("day12.txt")
    challenge12_new(input)