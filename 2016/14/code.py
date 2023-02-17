# Advent of code Year 2016 Day 14 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# input = "abc"
print(input)

import hashlib
def gethash(s):
    s = s.encode()
    h = hashlib.md5(s)
    hex = h.hexdigest()
    return hex

def gethash16(s):
    for _ in range(2017):
        s = s.encode()
        h = hashlib.md5(s)
        s = h.hexdigest()
    return s

def check_trip(s,l, t=None):
    n = len(s)
    for i in range(n-l+1):
        chars = s[i:i+l]
        targ = t if t else chars[0]
        if all(targ == c for c in chars):
            return chars[0]
    return None

def verify(s,i,t):
    for j in range(i+1,i+1000+1):
        check = s + str(j)
        if check_trip(gethash16(check), 5, t=t):
            return True 
    return False


# hashes = [gethash(input+str(i)) for i in range(1001)]


# i,keys = 0,0
# while keys < 64:
#     cand = hashes.pop(0)
#     trip = check_trip(cand,3)

#     if trip and any(check_trip(c,5,t=trip) for c in hashes):
#         print(f"Key {keys} is index {i}")
#         keys += 1

#     if keys == 64:
#         p1 = i 
#         break

#     hashes.append(gethash(input+str(i+1001)))
#     i += 1 


# print("Part One : "+ str(p1))

hashes = [gethash16(input+str(i)) for i in range(1001)]


i,keys = 0,0
while keys < 64:
    cand = hashes.pop(0)
    trip = check_trip(cand,3)

    if trip and any(check_trip(c,5,t=trip) for c in hashes):
        print(f"Key {keys} is index {i}")
        keys += 1

    if keys == 64:
        p2 = i 
        break

    hashes.append(gethash16(input+str(i+1001)))
    i += 1 


print("Part Two : "+ str(p2))