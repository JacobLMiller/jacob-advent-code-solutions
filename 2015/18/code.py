# Advent of code Year 2015 Day 18 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]


dirs = [1,-1,1j,-1j, 1+1j, -1+1j, 1-1j, -1-1j]

corners = [0, complex(0,len(input)-1), complex(len(input[0])-1, 0), complex(len(input[0])-1, len(input)-1)]

def update_grid(Grid,p2=False):
    G = {coord: sum([coord+d in Grid and Grid[coord+d] for d in dirs])
        for coord in Grid}
    for coord in Grid:
        if Grid[coord] and G[coord] not in (2,3): Grid[coord] = 0
        elif Grid[coord] == 0 and G[coord] == 3: Grid[coord] = 1
    if p2:
        for p in corners: Grid[p] = 1
    return Grid

def get_input():
    Grid = dict()
    for i, row in enumerate(input):
        for j, elem in enumerate(row):
            Grid[complex(j,i)] = 0 if elem == "." else 1
    return Grid

Grid = get_input()
for _ in range(100):
    Grid = update_grid(Grid)

p1 = sum(Grid.values())

print("Part One : "+ str(p1))

Grid = get_input()
for _ in range(100):
    Grid = update_grid(Grid,True)

p2 = sum(Grid.values())


print("Part Two : "+ str(p2))