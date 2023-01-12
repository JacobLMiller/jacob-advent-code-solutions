# Advent of code Year 2016 Day 2 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]


dir_map = {
    "D": 1j,
    "U": -1j,
    "L": -1,
    "R": 1
}

"""
123     -1-1j, 0-1j, 1-1j,
456     -1+0j, 0+0j, 1+0j,
789     -1+1j, 0+1j, 1+1j
"""
pos_map = {
    -1-1j: 1,
    0-1j: 2,
    1-1j: 3,
    -1: 4,
    0: 5,
    1: 6,
    -1+1j: 7,
    1j: 8,
    1+1j: 9 
}

code = list()
pos = 0
for line in input:
    instr = [dir_map[c] for c in line]
    for d in instr:
        if pos+d in pos_map:
            pos += d 
    code.append(str(pos_map[pos]))


print("Part One : "+ str("".join(code)))

"""
  1
 234
56789
 ABC
  D
"""
pos_map2 = {
    -2j: "1",
    -1 -1j: "2",
    -1j: "3",
    1-1j: "4",
    -2: "5",
    -1: "6",
    0: "7",
    1: "8",
    2: "9",
    -1+1j: "A",
    1j: "B",
    1+1j: "C",
    2j: "D"
}

code = list()
pos = -2
for line in input:
    instr = [dir_map[c] for c in line]
    for d in instr:
        if pos+d in pos_map2:
            pos += d 
    code.append(pos_map2[pos])

print("Part Two : "+ str("".join(code)))