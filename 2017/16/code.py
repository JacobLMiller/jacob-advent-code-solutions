# Advent of code Year 2017 Day 16 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split(",")



# swap = lambda L,s: L[-s:] + L[:-s]
def swap(L,s):
    # print(L)
    return L[-s:] + L[:-s]

def exchange(L,a,b):
    L[a], L[b] = L[b], L[a]
    return L
def partner(L,a,b):
    i,j = L.index(a), L.index(b)
    return exchange(L,i,j)

def parse(inp):
    cmd, pred = inp[0], inp[1:]
    if cmd == "s":
        return lambda x : swap(x, int(pred))
    p1, p2 = pred.split("/")
    if cmd == "x":
        return lambda x : exchange(x,int(p1), int(p2))
    return lambda x : partner(x, p1, p2)


instrlist = [parse(inp) for inp in input]


programs = list("abcdefghijklmnop")

for cmd in instrlist:
    programs = cmd(programs)



print("Part One : "+ str("".join(programs)))


instrlist = [parse(inp) for inp in input]
programs = list("abcdefghijklmnop")

seen = dict()

flag = True
count = 0
rep = 0
while(flag):
    for i,cmd in enumerate(instrlist):
        pair = ("".join(programs), i)
        seen[pair] = count
        programs = cmd(programs)
        count += 1
        if ("".join(programs), i+1) in seen:
            flag = False
            break
    rep += 1

programs = list("abcdefghijklmnop")
for j in range(1_000_000_000 % (rep-1)):
    for i,cmd in enumerate(instrlist):
        programs = cmd(programs)


print("Part Two : "+ "".join(programs))