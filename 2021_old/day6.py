import numpy as np

def read_input(path):
    myfile = open(path, "r")
    e = eval(myfile.readline())
    return list(e)

def part1(data):

    counts = {i: data.count(i) for i in range(9)}    
    for _ in range(256):
        zeros = counts[0]
        for i in range(1,9):
            counts[i-1] = counts[i]
        counts[6] += zeros 
        counts[8] = zeros

    print(sum(counts.values()))

    

if __name__ == "__main__":
    input = read_input("day6.txt")
    part1(input)