import numpy as np

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

class Node():
    def __init__(self,id,num,next,prev):
        self.id = id 
        self.num = num 
        self.next = next
        self.prev = prev

class List():
    def __init__(self,array):
        self.array = array
        self.n = len(array)
        self.idx0 = 0 
        for i,N in enumerate(self.array):
            if N.num == 0:
                self.idx0 = i
                break
    
    def print_list(self,idx=0):
        head = self.array[idx]
        for _ in range(self.n):
            print(head.num, end=", ")
            head = head.next
        print()
        

    def find_3000(self):
        head = self.array[ self.idx0 ]
        v = 0
        for i in range(3001):
            if i > 0 and i % 1000 == 0: 
                v += head.num 
            head = head.next
        return v

    def shift_list(self,id):
        og = self.array[id]
        start = og
        tmp = start.num 
        num = start.num
        # num_shift = tmp if tmp >= 0 else (self.n - id) + ()
        # print(num_shift)
        if num == 0: return
            
        i = 0
        if num >= 0:
            while i < abs(num):
                start = start.next
                i += 1
        else:
            while i >= num:
                start = start.prev 
                i -= 1
        
        og_next = og.next 
        og_prev = og.prev 

        tmp = start.next 
        start.next = og 
        og.next = tmp 

        og.prev = start 
        tmp.prev = og 

        og_next.prev = og_prev
        og_prev.next = og_next


        



def day20(data,repeat=1,mult=1):
    data = [int(d) for d in data]
    
    tup_list = [(i,d*mult) for i,d in enumerate(data)]

    n = len(tup_list)

    for _ in range(repeat):
        for i in range(n):
            for j in range(n):
                if tup_list[j][0] == i:
                    id,num = tup_list.pop(j)
                    if num == -j:
                        tup_list.append( (id,num) )
                    else:
                        tup_list.insert( (j+num)%(n-1), (id,num)  )
                    break
    
    id0 = 0 
    for i,num in enumerate(tup_list):
        if num[1] == 0:
            id0 = i 
            break 
    print(id0)
    one = tup_list[ (id0+1000)%(n) ][1]
    two = tup_list[ (id0+2000)%(n) ][1] 
    three = tup_list[ (id0+3000)%(n) ][1]    
    print( one+two+three )

if __name__ == "__main__":
    input = read_input("day20.txt")
    day20(input)
    day20(input, 10, 811589153)

