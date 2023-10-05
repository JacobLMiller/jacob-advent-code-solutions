# Advent of code Year 2017 Day 14 solution
# Author = ?
# Date = December 2018

class Node():
    def __init__(self,num):
        self.num = num 
        self.next = None 
    
    def set_next(self,next):
        self.next = next 

class List():
    def __init__(self, head):
        self.head = head
        self.skip = 0
        self.set_prev()
        self.tot_move = 0

    def _move_head(self,n):
        cur,l = self.head, 0
        while l < n:
            cur = cur.next
            l += 1
        self.head = cur

    def move_head(self,L):
        self._move_head(L+self.skip)
        self.tot_move += (L + self.skip)        
        self.skip += 1


    def set_prev(self):
        cur = self.head 
        while cur.next != self.head:
            cur = cur.next
        self.prev = cur

    def tolist(self):
        cur = self.head 
        out = list() 
        while cur.next != self.head:
            out.append(cur.num)
            cur = cur.next
        out.append(cur.num)
        return out
        
        

    def hash(self,L):
        if L < 1: 
            self.move_head(0)
            self.set_prev()
            return
        
        S = list()
        l = 0
        cur = self.head
        while l < L:
            S.append(cur)
            cur = cur.next
            l += 1

        end = cur
        cur = self.prev
        self.head = S[-1]
        while S:
            top = S.pop() 
            cur.next = top
            cur = top

        cur.next = end
        if cur == end:
            cur.next = self.prev

        self.move_head(L)
        self.set_prev()

def knothash(string):

    l = [Node(i) for i in range(256)]

    # l = [Node(s) for s in range(5)]

    cur_node = l[0]
    for i in range(len(l)):
        l[i].set_next(l[ (i+1) % len(l) ])
    # l[-1].set_next = cur_node

    def print_list(p2):
        cur = p2.head
        i = 0
        while i < len(l):
            print(f"{cur.num} -> ", end="")
            cur = cur.next
            i += 1
        print()    


    p2 = List(l[0])

    lengths = [ord(s) for s in string] + [17, 31, 73, 47, 23]
    for _ in range(64):
        for length in lengths:
            p2.hash(length)
    p2._move_head(len(l) - (p2.tot_move % len(l)))


    from functools import reduce
    out = p2.tolist()
    s = ""
    for i in range(0,256,16):
        x = reduce(lambda x,y: x^y, out[i:i+16])
        x = hex(x).replace("0x", "")
        if len(x) < 2: 
            x = "0" + x
        s += x
    return s


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

from tqdm import tqdm
grid = ""
for i in tqdm(range(128)):
    news = f"{input}-{i}"
    hash = knothash(news)
    bin_rep = ""
    for s in hash:    
        t = bin( int(s, 16) ).replace("0b", "")
        x = "0" * (4-len(t)) + t
        bin_rep += x

    grid += bin_rep


print("Part One : "+ str(sum(int(n) for n in grid)))

def bfs(G, source):
    visited = {source}
    Q = [source]

    while Q:
        cur = Q.pop()

        for dir in [1, -1, 1j, -1j]:
            check = cur + dir 
            if check in G and check not in visited:
                Q.insert(0,check)

        if cur not in visited:
            visited.add(cur)

    return visited

grid = [list(grid[i:i+128]) for i in range(0,128*128, 128)]
grid = {complex(i,j) for j in range(128) for i in range(128) if grid[i][j] == "1"}

visited = set()
components = 0
for src in grid:
    if src not in visited:
        component = bfs(grid,src)
        visited.update(component)
        components += 1


print("Part Two : " + str(components))