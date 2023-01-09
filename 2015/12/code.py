# Advent of code Year 2015 Day 12 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

import json 

data = json.loads(input)

def sum_nums(obj):
    if type(obj) == list:
        return sum([sum_nums(o) for o in obj])
    elif type(obj) == dict:
        return sum([sum_nums(o) for o in obj.values()])
    elif type(obj) == int:
        return obj 
    return 0

tot = sum_nums(data)




print("Part One : "+ str(tot))

def help(obj):
    if type(obj) == list:
        return sum([sum_nums(o) for o in obj])
    elif type(obj) == dict:
        if 'red' in obj.values(): return 0
        return sum([sum_nums(o) for o in obj.values()])
    elif type(obj) == int:
        return obj 
    return 0

tot = help(data)


print("Part Two : "+ str(tot))