# Advent of code Year 2016 Day 17 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# input = "ihgpwlah"

import hashlib

def bfs(s,t,input,p1=True):
    valid = set("bcdef")

    directions = [("U",0-1j), ("D",0+1j), ("L",-1+0j), ("R",1+0j)]
    
    Q = [(s,input)]
    parents = {(s,input): None}
    visited = {(s,input)}

    max_len = 0
    while Q:
        pos,path = Q.pop(0)
        if pos == t: 
            if p1: return path
            max_len = max(max_len, len(path) - len(input))
            continue
            # print(max_len)

        code = hashlib.md5(path.encode()).hexdigest()[:4]
        for c, (p_str,dir) in zip(code, directions):
            if c in valid:
                new_pos = pos + dir 
                new_path = path + p_str
                new_obj = (new_pos,new_path)
                if new_obj not in visited and 0 <= new_pos.real < 4 and 0 <= new_pos.imag < 4:
                    Q.append(new_obj)
                    visited.add(new_obj)


    return max_len
        


p1 = bfs(0+0j,3+3j,input)

print("Part One : "+ str(p1[len(input):]))

p2 = bfs(0+0j,3+3j, input, p1=False)

print("Part Two : "+ str(p2))