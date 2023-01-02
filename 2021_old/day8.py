def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

let_map = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

len_map = {
    i: len(val) for i,val in let_map.items()
}

"""
known: 1,4,7,8
0: 
2: {e,g} + {a}
3: 
4: given 
5: 8 - {c,e}
6: 8 - c
7: given
8: given
9: (4 U 7) U g

{c,f} = 1 
{a,c,f} = 7 
{a} = 7 - 1

{b,d} = 4 - 1
{d} = (3 I 4) - 1
{b} = 8 - {d U 7 U {e,g}

{g} = 3 - {a U 4} 

0 = 8 - {d}

{e,g} = (8 - (7 U 4))
a = 7 - 1 
b = 8 - (2+f)
c = 1 - f
d = 4 - (1 U b)
e = count 3
f = count 9
g = {e,g} - e

3 = 8 - (7 U d U e)
"""

def day8_1(data):
    data = [d.split("|")[1].lstrip() for d in data]

    unq = [2,4,3,7]
    c = 0
    for s in data:
        for comb in s.split(" "):
            if len(comb) in unq: 
                c += 1
    print(f"Day 8 Part 1: {c}")

def evaluate(nums, vals):
    print(nums, vals)
    nums = [n.strip() for n in nums.split(" ")[:-1]]
    vals = [set(n.strip()) for n in vals.split(" ")[1:]]
    lets = {c: None for c in 'abcdefg'}
    num_map = dict()

    counts = {c: 0 for c in "abcdefg"}
    for i, n in enumerate(nums):
        if len(n) == 2:
            num_map[1] = set(n)
        if len(n) == 4:
            num_map[4] = set(n)
        if len(n) == 3:
            num_map[7] = set(n)
        if len(n) == 7: 
            num_map[8] = set(n)
        for c in n:
            counts[c] += 1
    
    e,f = None, None 
    for c in counts:
        if counts[c] == 4: e = set(c)
        if counts[c] == 9: f = set(c) 
    a = num_map[7] - num_map[1]
    c = num_map[1] - f 
    num_map[5] = num_map[8] - (c.union(e))
    comp_5 = num_map[8] - num_map[5]
    for n in nums:
        tmp = num_map[8] - set(n)
        if len(tmp) == 1 and list(e)[0] in n and list(c)[0] in n:
            d = tmp

    e_g = num_map[8] - num_map[7].union(num_map[4])
    g = e_g - e
    b = num_map[4] - c.union(f).union(d)
    
    num_map[0] = num_map[8] - d 
    num_map[2] = num_map[8] - b.union(f)
    num_map[3] = num_map[8] - b.union(e)
    num_map[6] = num_map[8] - c 
    num_map[9] = num_map[8] - e

    map_num = {frozenset(s): str(n) for n,s in num_map.items()}

    kl = "".join(map_num[frozenset(s)] for s in vals)

    return int(kl)

def day8_2(data):
    data = [d.split("|") for d in data]
    print(data)

    # c_map = {c: 0 for c in "abcdefg"}
    # for s in data[0].split(" "):
    #     print(set(s))
    
    # for c,val in c_map.items():
    #     print(f"{c}: {val}")

    p2 = sum( [evaluate(d, v) for d, v in data] )
    print(f"Day 8 part 2: {p2}")

if __name__ == "__main__":
    input = read_input('day8.txt')
    day8_2(input)