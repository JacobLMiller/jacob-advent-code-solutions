def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return [[int(d) for d in row] for row in lines]

def tuple_add(p1,p2):
    return (p1[0] + p2[0], p1[1] + p2[1])



import heapq
def astar(s,t,weights):
    n = len(weights)

    def h(x,t=(n-1,n-1)):
        return abs(x[0]-t[0]) + abs(x[1]-t[1])    

    Q = [s]
    explored = {s}
    g_dst = {s: 0}
    f_dst = [(h(s), s)]
    heapq.heapify(f_dst)

    dirs = [(0,1), (1,0), (-1, 0), (0,-1)]

    # def visit_node(u,v,cost):
    #     dst[u] = dst[v] + cost
    #     explored.add(u)
    #     Q.insert(0,u)

    while f_dst[0]:
        _,v = heapq.heappop(f_dst) 
        if v == t: return g_dst[v]

        for dir in dirs:
            x,y = tuple_add(v, dir)
            if 0 <= x <= n-1 and 0 <= y <= n-1:
                tmpdst = g_dst[v] + weights[x][y]
                if (x,y) not in g_dst or tmpdst < g_dst[(x,y)]:
                    g_dst[(x,y)] = tmpdst
                    heapq.heappush( f_dst, (tmpdst + h((x,y)), (x,y)) )


    # return dst[t]


def day15(data):
    n = len(data)
    s = (0,0)
    t = (n-1,n-1)
    d = astar(s,t,data)
    print(d)

    #part2 
    W = [[data[i][j] if i < n and j < n else 0 for j in range(n*5)] for i in range(n*5)]
    #Fill first column block
    for i in range(n):
        for j in range(n,5*n):
            W[j][i] = (W[j-n][i] + 1) % 10
            if W[j][i] == 0: W[j][i] = 1

    #Fill the rest 
    for i in range(n*5):
        for j in range(n,n*5):
            W[i][j] = (W[i][j-n] + 1) % 10
            if W[i][j] == 0: W[i][j] = 1
    
    d = astar(s, (n*5-1,n*5-1), W)
    print(d)


if __name__ == "__main__":
    input = read_input("day15.txt")
    day15(input)