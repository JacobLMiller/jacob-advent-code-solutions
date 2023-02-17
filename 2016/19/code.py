# Advent of code Year 2016 Day 19 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = int(input_file.read())

# input = 5

class Elf():
    def __init__(self,val):
        self.value = val
        self.next = None

def find_elf(num):
    curr = Elf(1)
    start = curr 
    for i in range(2,num+1):
        curr.next = Elf(i)
        curr = curr.next

    curr.next = start
    curr = start 

    while curr.next != curr: 
        curr.next = curr.next.next 
        curr = curr.next 
    return curr.value


p1 = find_elf(input)
print("Part One : "+ str(p1))


from numba import jit

@jit
def get_p2(n):
    w = 1 
    for i in range(1,n):
        w = w % i + 1
        if w > (i+1)/2:
            w += 1
    return w

p2 = get_p2(input)
print("Part Two : "+ str(p2))