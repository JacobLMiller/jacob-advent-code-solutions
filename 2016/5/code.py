# Advent of code Year 2016 Day 5 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# input = "abc"

import hashlib

# i = 0
# p1 = list()
# while True:
#     s = input + str(i)
#     s = s.encode()
#     hash = hashlib.md5(s)

#     hex = hash.hexdigest()
#     if hex[:5] == "00000":
#         print(hex[5])
#         p1.append(hex[5])
#         if len(p1) == 8:
#             break

#     i += 1


# print("Part One : "+ str("".join(p1)))

i = 0
p2 = [None] * 8
print(p2)
while True:
    s = input + str(i)
    s = s.encode()
    hash = hashlib.md5(s)

    hex = hash.hexdigest()
    if hex[:5] == "00000":
        p,c = hex[5], hex[6]
        if p.isdigit() and 0 <= int(p) < 8 and p2[int(p)] != None:
            p2[int(p)] = c
            print(p2)
        if all(p2):
            break

    i += 1

print("Part Two : "+ str(None))