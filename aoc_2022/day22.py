def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

jumplist = dict()

#top right block
for y in range(50):
    jumplist[complex(150,y)] = complex(50,y)
    jumplist[complex(49,y)] = complex(149,y)

#middle top block 
for y in range(50,100):
    jumplist[complex(100,y)] = complex(50,y)
    jumplist[complex(49,y)] = complex(99,y)

for y in range(100,150):
    jumplist[complex(100,y)] = complex(0,y)
    jumplist[complex(-1,y)] = complex(99,y)

for y in range(150,200):
    jumplist[complex(50,y)] = complex(0,y)
    jumplist[complex(-1,y)] = complex(49,y)


for x in range(100,150):
    jumplist[complex(x,-1)] = complex(x,49)
    jumplist[complex(x,50)] = complex(x,0)

for x in range(50,100):
    jumplist[complex(x,-1)] = complex(x,149)
    jumplist[complex(x,150)] = complex(x,0)

for x in range(0,50):
    jumplist[complex(x,99)] = complex(x,199)
    jumplist[complex(x,200)] = complex(x,100)


"""
 21
 3
54
6
"""

"""
0: right, 
1: down, 
2: left, 
3: up
"""

def jump_cube(p,d):
    x,y = p.real, p.imag 
    #above 1 goes to above 6
    if y < 0 and 100 <= x <= 149:
        return complex(x-100, 199), 3
    #right 1 goes to left 4
    if 0 <= y <= 49 and x > 149:
        return complex(99, y+100), 2
    #down 1 goes to left 3
    if 100 <= x <= 149 and y > 49:
        return complex(99, x-50),  2

    #above 2 goes to right 6
    if 50 <= x <= 99 and y < 0:
        return complex(0,x+100), 0

    #left 2 goes to right 5 
    if x < 50 and 0 <= y <= 49:
        return complex(0, y-100), 0

    #right 3 goes to up 1 
    if x > 99 and 50 <= y <= 99:
        return complex(y+50, 49), 3

    #left 3 goes to down 5 
    if x < 50 and 50 <= y <= 99:
        return complex(y-50,100), 1

    #right 4 goes to left 1 
    if x > 99 and 100 <= y <= 149:
        return complex(149, y - 100), 2

    #down 4 goes to left 6 
    if 50 <= x <= 99 and y > 149:
        return complex(49, x+100), 2

    #up 5 goes to right 3 
    if 0 <= x <= 49 and y < 100:
        return complex(50, y-50 ), 0

    #left 5 goes to right 2 
    if x < 0 and 100 <= y <= 149:
        return complex(50, y-100), 2

    #right 6 goes to up 4 
    if x > 49 and 150 <= y <= 199:
        return complex(y-100,149), 3

    #down 6 goes to down 1 
    if 0 <= x <= 49 and y > 199:
        return complex(x+100, 0), 1

    # left 6 goes to down 2
    if x < 0 and 150 <= y <= 199:
        return complex(y-100,0), 1
    
    print("yu oh")
    print(p)


def day22(map, directions,part2=False):
    w = max([len(r) for r in map])
    h = len(map)
    # map = [r.replace(" ", "") for r in map]

    for row in map:
        print(row)

    wallset = set()
    tileset = set()
    emptyset = set()
    start = None
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#": wallset.add(complex(j,i))
            elif map[i][j] == ".": 
                tileset.add(complex(j,i))
                if not start: start = complex(j,i)
            elif map[i][j] == " ": emptyset.add(complex(j,i))
            else: print("uh oh")
    for i in range(w):
        for j in range(h):
            if complex(i,j) not in tileset and complex(i,j) not in wallset:
                emptyset.add(complex(i,j))
 
    
    instr_set = directions.strip().replace("R", ",R,").replace("L",",L,")
    facing = {
        0: 1 + 0j, #facing right
        1: 0 + 1j, #facing down 
        2: -1 + 0j, #facing left 
        3: 0 - 1j #facing up
    }
    face = 0
    pos = start
    print(instr_set.split(",")[:10])
    print(-1%4)
    for instr in instr_set.split(","):
        if instr == "R":
            face = (face+1) % 4
        elif instr == "L":
            face = (face-1) % 4
        else:
            num = int(instr)
            c = 0
            step = facing[face]
            moving = True 
            while moving and c < num:
                tmp = pos + step 
                if tmp in jumplist: 
                    if part2:
                        tmp, face = jump_cube(tmp,face)
                    else: tmp = jumplist[tmp]
                    
                if tmp in wallset:
                    moving = False
                    break 
                elif tmp in tileset:
                    pos = tmp
                elif tmp in emptyset:
                    print("hopefully no there") 
                
                c += 1

    print(pos)
    #The final password is the sum of 1000 times the row, 4 times the column, and the facing
    print(f"Day 22 part 1: {int(1000*(pos.imag+1) + 4 * (pos.real+1) + face)}")

if __name__ == "__main__":
    input = read_input("day22.txt")
    map = input[:-2]
    directions = input[-1]

    day22(map,directions)
    day22(map,directions,True)