import numpy as np 

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines


def day18(data):
    data = [row.split(",") for row in data]
    data = [(int(x), int(y), int(z)) for x,y,z  in data]
    num_sides = 0
    coords = set(data)
    for x,y,z in coords:
        sides = 6
        if (x-1, y,z) in coords:
            sides -= 1
        if (x+1, y,z) in coords:
            sides -= 1
        if (x, y-1,z) in coords:
            sides -= 1
        if (x, y+1,z) in coords:
            sides -= 1
        if (x,y, z-1) in coords: 
            sides -= 1
        if (x,y,z+1) in coords:
            sides -= 1

        num_sides += sides
    
    print(num_sides)

    def adj_cubes(p):
        x,y,z = p 
        yield x+1, y, z
        yield x-1, y, z 
        yield x, y+1, z
        yield x, y-1, z 
        yield x, y, z+1 
        yield x, y, z-1

    all_cubes = {(x,y,z) for x in range(20) for y in range(20) for z in range(20)}
    empty_cubes = all_cubes-coords
    print(empty_cubes)
    q = [(0,0,0)]
    while q:
        c = q.pop()
        if c in empty_cubes:
            empty_cubes.remove(c)
            q.extend(adj_cubes(c))    

    for p in empty_cubes:
        num_sides += 6 
        for adj in adj_cubes(p):
            if adj in coords:
                num_sides -= 2
        coords.add(p)
    print(num_sides)


if __name__ == "__main__":
    input = read_input("day18.txt")
    day18(input)