def read_input(path):
    myfile = open(path, "r")
    e = eval(myfile.readline())
    return list(e)

data = read_input("day7.txt")

mi = min(data)
ma = max(data)

norm = 100000000
for y in range(mi,ma+1):
    s = sum([abs(d-y) for d in data])
    if s < norm: 
        norm = s

print(f"day 7 part 1: {norm}")

norm = 100000000
for y in range(mi,ma+1):
    s = sum([sum([r for r in range(abs(d-y)+1)]) for d in data])
    if s < norm: 
        norm = s
print(f"day 7 part 2: {norm}")