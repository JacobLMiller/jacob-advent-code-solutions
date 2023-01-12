# Advent of code Year 2016 Day 4 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip().replace("]","").split("-") for d in input_file.readlines()]

char_map = dict(zip(
    list("abcdefghijklmnopqrstuvwxyz"),
    range(26,-1,-1)
))

class CodeCount():
    def __init__(self,s):
        self.counter = {c:0 for c in set(s)}
        for c in s:
            self.counter[c] += 1
    def is_valid(self,hash):
        tup = list(self.counter.items())
        tup = sorted(tup, key = lambda x: (x[1],char_map[x[0]]),reverse=True)[:5]

        if all([h == t for h,t in zip(hash,[x[0] for x in tup])]):
            return True 
        return False

p1 = 0
valid_codes = list()
for s in input:
    codes = "".join(s[:len(s)-1])
    hash = s[-1]

    id,hash = hash.split("[")

    C = CodeCount(codes)
    if C.is_valid(hash): 
        valid_codes.append(s)
        p1 += int(id)

print("Part One : "+ str(p1))

char_map = dict(zip( 
    list("abcdefghijklmnopqrstuvwxyz"),
    range(26)
))

num_map = dict(zip( 
    range(26),
    list("abcdefghijklmnopqrstuvwxyz")
))

def get_char(c,shift):
    if c == " ": return " "
    n = char_map[c]
    n = (n+shift) % 26
    return num_map[n]


for s in valid_codes:
    code = " ".join(s[:len(s)-1])
    shift, hash = s[-1].split("[")

    decrypt = [get_char(c,int(shift)) for c in code]

    decrypt = "".join(decrypt)
    if "north" in decrypt:
        p2 = shift


print("Part Two : "+ str(p2))