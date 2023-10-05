# Advent of code Year 2017 Day 10 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [int(d) for d in input_file.readlines()[0].split(",")]

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
        
        

l_size = 256

cur_node = Node(0)

old = cur_node
for n in range(1,l_size):
    new = Node(n)
    old.set_next(new)
    old = new 
old.set_next(cur_node)

p1 = List(cur_node)

lengths = input
for l in lengths:
    p1.hash(l)

p1._move_head(l_size - (p1.tot_move % l_size))

ans = p1.head.num * p1.head.next.num



print("Part One : "+ str(ans))

l_size = 4

inp = "1,2,3"
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
        s += hex(x).replace("0x", "")
    return s

p2 = knothash(",".join(str(n) for n in input))
print("Part Two : "+ str(p2))