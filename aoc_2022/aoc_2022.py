import numpy as np

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

def challenge1(data):
    max_sum,cur_sum = 0,0
    for line in data:
        if line != "\n":
            cur_sum += int(line.strip("\n"))
        else:
            max_sum = max(cur_sum, max_sum)
            cur_sum = 0
    print(max_sum)

    ##Part2 
    sums,cur_sum = [], 0
    for line in data:
        if line != "\n":
            cur_sum += int(line.strip("\n"))
        else:
            sums.append(cur_sum)
            cur_sum = 0
    top_3 = sorted(sums,reverse=True)[:3]
    print(sum(top_3))
            

def challenge2(path):
    data = np.loadtxt(path,dtype="U10").tolist()

    def who_wins(A,B):
        if A == B: 
            return 3
        if A == 0:
            if B == 1:
                return 6
            else: return 0
        if A == 1:
            if B == 2: 
                return 6
            else: return 0 
        if A == 2: 
            if B == 0: 
                return 6
            else: return 0
    
    letter_map = {
        'A': 0, 
        'B': 1, 
        'C': 2,
        "X": 0, 
        "Y": 1, 
        "Z": 2
    }
    point_map = {
        "X": 1, 
        "Y": 2, 
        "Z": 3
    }

    score = sum(
        [point_map[b] + who_wins(letter_map[a],letter_map[b]) for a,b in data]
    )
    print(score)

    ##Part 2 

    point_map = {"X": 0, "Y": 3, "Z": 6}
    tuple_map = {
        ("A","X"): 3,
        ("A","Y"): 1,
        ("A","Z"): 2,
        ("B","X"): 1,
        ("B","Y"): 2,
        ("B","Z"): 3,
        ("C","X"): 2,
        ("C","Y"): 3,
        ("C","Z"): 1,
    }
    score = sum(
        [point_map[b] + tuple_map[(a,b)] for a,b in data]
    )
    print(score)

def challenge3(data):
    mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valmap = dict(zip(list(mystr), [i for i in range(1,26+26+1)]))
    data = [l.strip("\n") for l in data]

    p = 0
    for item in data:
        n = len(item)
        part1,part2 = set(item[:n//2]), set(item[n//2:])
        p += valmap[ ''.join(part1.intersection(part2)) ]
    print(p)

    #Part 2 
    p = 0
    for i in range(0,len(data),3):
        part1,part2,part3 = set(data[i]),set(data[i+1]),set(data[i+2])
        p += valmap[ ''.join(part1.intersection(part2).intersection(part3)) ]
    print(p)
        

def challenge4(data):
    pairs = [l.split(",") for l in data]
    pairs = [(f.split("-"), s.split("-")) for f,s in pairs]

    is_contained = lambda a,b: True if int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]) else False

    c = 0
    for a,b in pairs:
        if is_contained(a,b) or is_contained(b,a): c += 1
    print(c)

    #part 2
    is_overlap = lambda a,b: True if int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[0]) else False
    c = 0 
    for a,b in pairs:
        if is_overlap(a,b) or is_overlap(b,a): c += 1
    print(c)

og_stacks = [ 
    list("FDBZTJRN"),
    list("RSNJH"),
    list("CRNJGZFQ"),
    list("FVNGRTQ"),
    list("LTQF"),
    list("QCWZBRGN"),
    list("FCLSNHM"),
    list("DNQMTJ"),
    list("PGS")
]

"""
[N]     [Q]         [N]            
[R]     [F] [Q]     [G] [M]        
[J]     [Z] [T]     [R] [H] [J]    
[T] [H] [G] [R]     [B] [N] [T]    
[Z] [J] [J] [G] [F] [Z] [S] [M]    
[B] [N] [N] [N] [Q] [W] [L] [Q] [S]
[D] [S] [R] [V] [T] [C] [C] [N] [G]
[F] [R] [C] [F] [L] [Q] [F] [D] [P]
 1   2   3   4   5   6   7   8   9 
 """



def challenge5(path):
    # #of moves, stack1, stack2
    instr = [[int(s) for s in txt.split() if s.isdigit()] for txt in path]

    stacks = og_stacks.copy()
    for num_moves, s1, s2 in instr:
        for _ in range(num_moves):
            tmp = stacks[s1-1].pop()
            stacks[s2-1].append(tmp)
    print([s[-1] for s in stacks])

    ##Part 2
    stacks = og_stacks.copy()
    for num_moves, s1, s2 in instr:
        tmp = stacks[s1-1][-num_moves:]
        del stacks[s1-1][-num_moves:]
        stacks[s2-1] += tmp
    print([s[-1] for s in stacks])

def challenge6(data):
    data = data[0]
    n = len(data)
    for i in range(n-4):
        a,b,c,d = data[i],data[i+1],data[i+2],data[i+3]
        s = set((a,b,c,d))
        if len(s) == 4: 
            print(i+4)
            break

    ##Part 2
    for i in range(n-14):
        s = set(data[i:i+14])
        if len(s) == 14:
            print(i+14)
            break

class Tree():
    def __init__(self,name,parent):
        self.children = dict()
        self.size = 0
        self.parent = parent
        self.name = name
        # self.child_map = dict()

    def get_size(self):
        return self.size 

    def set_size(self):
        self.size = self.size + sum([child.set_size() for child in self.children.values()])
        return self.size

class Count():
    def __init__(self):
        self.count = 0
        self.min_cand = list()

def challenge7(data):
    T = Tree("/", None)

    cur_node = T
    for line in data:
        if line == "$ cd /": continue
        if line == "$ cd ..":
            cur_node = cur_node.parent 
            continue
        if "$ cd" in line:
            _,_,dir = line.split(" ")
            cur_node = cur_node.children[dir]
            continue
        s = line.split(" ")
        if s[0] == "dir":
            cur_node.children[s[1]] = Tree(s[1], cur_node)
        elif s[0].isnumeric():
            cur_node.size += int(s[0])
    
    T.set_size()
    #Traverse tree
    count = Count()
    def traverse_tree(root):
        if root.size <= 100000:
            count.count += root.size
        [traverse_tree(child) for child in root.children.values()]
        
    
    traverse_tree(T)
    print(count.count)


    ##Part 2
    unused = 70000000 - T.size
    needed = 30000000 - unused 

    def find_min(root):
        if root.size >= needed:
            count.min_cand.append(root.size)
        [find_min(child) for child in root.children.values()]
    find_min(T)
    print(min(count.min_cand))


def scenic_score(X,i,j):
    right,left,up,down = 1,1,1,1
    h = X[i,j]
    n = X.shape[0]

    #Calc right
    for jp in range(j+1,n):
        if X[i,jp] < h and jp != n-1: right += 1
        else: break 
    #Calc left
    for jp in range(j-1,-1,-1):
        if X[i,jp] < h and jp != 0: left += 1
        else: break          
    #Calc up
    for ip in range(i-1,-1,-1):
        if X[ip,j] < h and ip != 0: up += 1
        else: break     
    #Calc down
    for ip in range(i+1,n):
        if X[ip,j] < h and ip != n-1: down += 1
        else: break     

    return right*left*up*down

def challenge8(data):
    data = [[int(i) for i in d] for d in data]
    X = np.array(data)

    C = np.zeros(X.shape)
    for i in range(X.shape[0]):
        tallest = -1
        for j in range(X.shape[0]):
            if X[i,j] > tallest: C[i,j] = 1
            tallest = max(tallest,X[i,j])
        tallest = -1
        for j in range(X.shape[0]-1,-1,-1):
            if X[i,j] > tallest: C[i,j] = 1
            tallest = max(tallest,X[i,j])
        tallest = -1
        for j in range(X.shape[0]):
            if X[j,i] > tallest: C[j,i] = 1
            tallest = max(tallest,X[j,i])
        tallest = -1
        for j in range(X.shape[0]-1,-1,-1):
            if X[j,i] > tallest: C[j,i] = 1
            tallest = max(tallest,X[j,i])
    print(int(np.sum(C)))

    #Part 2
    C = np.zeros(X.shape)
    for i in range(1,X.shape[0]-1):
        for j in range(1,X.shape[0]-1):
            C[i,j] = scenic_score(X,i,j)
    print(int(np.max(C)))


class Knot():
    def __init__(self):
        self.x = 0
        self.y = 0

class Head(Knot):
    def move(self,instr):
        if instr == "U": self.y += 1
        elif instr == "R": self.x += 1
        elif instr == "D": self.y -= 1
        elif instr == "L": self.x -= 1

def update(H,T):
        x, y = H.x,H.y
        dist_x = x - T.x
        dist_y = y - T.y
        if abs(dist_x) == 2 and not dist_y: # horizontal
            xv = 1 if dist_x > 0 else -1
            T.x += xv
        elif abs(dist_y) == 2 and not dist_x: # vertical
            yv = 1 if dist_y > 0 else -1
            T.y += yv
        elif (abs(dist_y) == 2 and abs(dist_x) in (1, 2)) or (abs(dist_x) == 2 and abs(dist_y) in (1, 2)):
            xv = 1 if dist_x > 0 else -1
            T.x += xv
            yv = 1 if dist_y > 0 else -1
            T.y += yv
        

def challenge9(data):
    data = [d.split(" ") for d in data]
    instr = [(move, int(num)) for move,num in data]

    visited = set()
    H, T = Head(), Knot()
    for move, num in instr:
        for _ in range(num):
            H.move(move)
            update(H,T)
            visited.add( (T.x,T.y) )

            
    print(len(visited))

    #part 2
    visited = set()
    H = Head()
    Ts = [Knot() for _ in range(9)]
    for move, num in instr:
        for _ in range(num):
            H.move(move)
            update(H,Ts[0])
            [update(Ts[i], Ts[i+1]) for i in range(8)]
            visited.add( (Ts[8].x, Ts[8].y) )
    print(len(visited))

    
def challenge10(data):
    instr = data
    keep = [20,60,100,140,180,220]
    vals = list()
    i = 0
    cycle = 0
    X = 1
    wait = True
    while i < len(instr):
        cycle += 1
        if cycle in keep:
            vals.append(X * cycle)

        if instr[i] == "noop":
            i += 1
            continue 
        if wait: 
            wait = False 
            continue
        _,val = instr[i].split(" ")
        X += int(val)
        i += 1
        wait = True
    print(sum(vals))

    #Part 2
    X = 1
    cycle, i, wait = 0, 0, True
    row, column = 0, 0
    C = np.zeros((6,40))
    while i < len(instr):
        cycle += 1 
        if cycle >= 240: break
        
        if X == column or X-1 == column or X+1 == column:
            C[row,column] = 1

        column += 1 
        if column % 40 == 0:
            column = 0
            row += 1

        if instr[i] == "noop":
            i += 1
            continue 
        if wait: 
            wait = False 
            continue
        _,val = instr[i].split(" ")
        X += int(val)
        i += 1
        wait = True    


    C = C.astype(int).tolist()
    mapped = list()
    for row in C:
        mapped.append( ["#" if r else "." for r in row] )
    for row in mapped:
        mystr = ""
        for char in row:
            mystr += char 
        print(mystr)

mod_array = [
    19,
    13,
    5,
    7,
    17,
    2,
    3,
    11
]

class Monkey():
    def __init__(self,
        starting_items,
            op,
            test,
            true,
            false,
            ind):
        self.starting_items = starting_items 
        self.op = op 
        self.test = test 
        self.true = true 
        self.false = false
        self.mod_ind = ind
        self.count = 0

    def inspect(self,truedst,falsedst):
        for item in self.starting_items:
            self.count += 1

            item = self.op(item) 
            item = item // 3
            if self.test(item):
                self.goto(truedst,item)
            else:
                self.goto(falsedst,item)
        self.starting_items = list()

    def new_inspect(self,truedst,falsedst):
        for item in self.starting_items:
            self.count += 1
            item = [self.op(i) for i in item]
            item = [i % m for i,m in zip(item,mod_array)]
            if item[self.mod_ind]  == 0:
                self.goto(truedst,item)
            else: self.goto(falsedst,item)
        self.starting_items = list()
    
    def goto(self,dst,item):
        dst.starting_items.append(item)



def challenge11():
    from monkey import get_monkeys

    Monkeys = get_monkeys()

    for _ in range(20):
        for Mon in Monkeys:
            Mon.inspect( 
                Monkeys[Mon.true],
                Monkeys[Mon.false]
            )
    counts = [Mon.count for Mon in Monkeys]
    counts = sorted(counts,reverse=True)
    print(counts[0] * counts[1])

    #Part 2
    Monkeys = get_monkeys()

    for Mon in Monkeys:
        Mon.starting_items = [ 
            [item for _ in mod_array] for item in Mon.starting_items
        ]
        
    for _ in range(10000):
        for Mon in Monkeys:
            Mon.new_inspect( 
                Monkeys[Mon.true],
                Monkeys[Mon.false]
            )
    counts = [Mon.count for Mon in Monkeys]
    counts = sorted(counts,reverse=True)
    print(counts[0] * counts[1])



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
    
    input = read_input("day1.txt")
    challenge1(input)

    challenge2("day2.txt")

    input = read_input("day3.txt")
    challenge3(input)

    input = read_input("day4.txt")
    challenge4(input)

    input = read_input("day5.txt")
    challenge5(input)

    input = read_input("day6.txt")
    challenge6(input)

    input = read_input("day7.txt")
    challenge7(input)

    input = read_input("day8.txt")
    challenge8(input)

    input = read_input("day9.txt")
    challenge9(input)

    input = read_input("day10.txt")
    challenge10(input)

    challenge11()

    input = read_input("day12.txt")
    challenge12_new(input)
