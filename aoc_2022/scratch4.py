import numpy as np
import ast

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines


def compare_lists(l1,l2):
    
    n = len(l1)
    m = len(l2)

    for i in range(n):
        if i >= m: 
            return False
        u,v = l1[i], l2[i]
        if type(u) == int and type(v) == int:
            if u < v: return True 
            if u > v: return False 
            continue
        else: 
            if type(u) == int: u = [u]
            if type(v) == int: v = [v]
            if u == v: continue
            return compare_lists(u,v)

    return True

def sort_list(l):

    for i in range(len(l)-1):
        swapped = False
        for j in range(len(l)-1):
            if not compare_lists(l[j],l[j+1]):
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
                swapped = True
        if not swapped:
            break
   
    return l


def challenge13(data):
    struct = list()
    tot = 0
    for c,i in enumerate(range(0,len(data),3)):
        up = ast.literal_eval(data[i])
        down = ast.literal_eval(data[i+1])

        # if len(up) == 0: correct = False
        correct = compare_lists(up,down)

        struct.append(up)
        struct.append(down)

        if correct: 
            tot += (c+1)
    print(tot)

    struct.append([[2]])
    struct.append([[6]])

    struct = sort_list(struct)
    
    first = struct.index([[2]]) + 1
    second = struct.index([[6]]) + 1
    print(first*second)

if __name__ == "__main__":
    input = read_input("day13.txt")
    challenge13(input)

    # u = [[1],[2,3,6]]
    # v = [[1],1]

    # print(compare_lists(u,v))