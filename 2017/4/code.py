# Advent of code Year 2017 Day 4 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip().split(' ') for d in input_file.readlines()]


p1 = 0 
for passcode in input:
    words = set(passcode)
    if len(words) == len(passcode): p1 += 1

print("Part One : "+ str(p1))

p2 = 0 
char_map = dict(zip( 
    "abcdefghijklmnopqrstuvwxyz",
    range(26)
))
for passcode in input:
    words = [[0 for _ in range(26)] for word in passcode]
    for i,word in enumerate(passcode):
        for j, c in enumerate(word):
            words[i][char_map[c]] += 1

    words = {tuple(word) for word in words}
    if len(words) == len(passcode): p2 += 1


print("Part Two : "+ str(p2))