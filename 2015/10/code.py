# Advent of code Year 2015 Day 10 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = list(input)

def step(num):
    data = list()

    cur = num[0]
    count = 0
    for c in num:
        if cur == c:
            count += 1
        else:
            data += [str(count), cur]
            cur = c 
            count = 1
    else:
        data += [str(count), cur]
    
    return data

ans = input
for _ in range(40):
    ans = step(ans)

print("Part One : "+ str(len(ans)))

for _ in range(10):
    ans = step(ans)

print("Part Two : "+ str(len(ans)))