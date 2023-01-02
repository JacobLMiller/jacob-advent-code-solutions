def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [list(l.strip("\n")) for l in lines]
    return lines

def BFS(s,world):
    Q = [s]
    visited = {s}

    dirs = {-1, 1, -1j, 1j}

    while len(Q) > 0:
        v = Q.pop()
        for d in dirs: 
            if v+d not in visited and v+d in world \
                and world[v+d] == world[v] + 1 and world[v+d] != 9:
                visited.add(v+d)
                Q.insert(0,v+d)
    
    return len(visited)




data = read_input("day9.txt")
data = [[int(d) for d in row] for row in data]


h = len(data)
w = len(data[0])
d_map = dict()
#Check top 
for j in range(w):
    for i in range(h):
        d_map[complex(j,i)] = data[i][j]

dirs = {-1, 1, -1j, 1j}

lows = 0
low_p = set()
for p,h in d_map.items():
    if all([d_map[p+d] > h for d in dirs if p+d in d_map]):
        lows += (1+h)
        low_p.add(p)
print(lows)

#part 2

sizes = [BFS(s,d_map) for s in low_p]

sizes = sorted(sizes,reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
