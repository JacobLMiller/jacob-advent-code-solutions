# Advent of code Year 2015 Day 16 solution
# Author = ?
# Date = December 2022

Correct_Aunt = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    input = [d.replace("Sue ","")
            .replace(": ", ",")
            .replace(" ","")
            for d in input]


CA = [d.split(":") for d in Correct_Aunt.split("\n")]
CA = {prop: int(val) for prop, val in CA}

class Aunt():
    def __init__(self,s):
        print(s)
        id, prop1, val1, prop2, val2, prop3, val3 = s.split(",")

        self.props = dict()
        self.props[prop1] = int(val1)
        self.props[prop2] = int(val2)
        self.props[prop3] = int(val3)

        self.id = int(id)
    
    def compare(self):
        for key in self.props.keys():
            if self.props[key] != CA[key]:
                return False
        return True

    def compare2(self):
        for key in self.props.keys():
            #Greater than
            if key in ['cats', 'trees']:
                if self.props[key] <= CA[key]: return False
            elif key in ['pomeranians', 'goldfish']:
                if self.props[key] >= CA[key]: return False
            else:
                if self.props[key] != CA[key]: return False 
        return True


p1 = None
p2 = None
for inp in input:
    A = Aunt(inp)
    if A.compare(): p1 = A.id
    if A.compare2(): p2 = A.id

print("Part One : "+ str(p1))



print("Part Two : "+ str(p2))