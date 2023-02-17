# Advent of code Year 2016 Day 6 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]


n = len(input[0])

gen_dict = lambda: {c: 0 for c in list("abcdefghijklmnopqrstuvwxyz")}

counts = [gen_dict() for _ in range(n)]

for s in input:
    for i,c in enumerate(s):
        counts[i][c] += 1

p1 = [max(count, key=count.get) for count in counts]

print("Part One : "+ str("".join(p1)))

p2 = [min(count, key=count.get) for count in counts]

print("Part Two : "+ str("".join(p2)))