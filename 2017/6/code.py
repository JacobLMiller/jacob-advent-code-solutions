# Advent of code Year 2017 Day 6 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

blocks = [int(d) for d in input.split('\t')]
# blocks = [0,2,7,0]


def get_max(arr):
    m,i = arr[0], 0
    for j,val in enumerate(arr[1:]):
        if val > m: 
            m = val 
            i = j+1 
    return m,i

def find_repeat(blocks):
    seen = {tuple(blocks)}
    p1 = 0
    n = len(blocks)

    while True:
        steps, start = get_max(blocks)
        blocks[start] = 0
        for offset in range(steps):
            ind = (offset+start+1) % n
            blocks[ind] += 1
        p1 += 1
        curr = tuple(blocks)
        if curr in seen:
            break
        seen.add(curr)
    return p1, blocks

p1, blocks = find_repeat(blocks)

print("Part One : "+ str(p1))

p2, blocks = find_repeat(blocks)

print("Part Two : "+ str(p2))