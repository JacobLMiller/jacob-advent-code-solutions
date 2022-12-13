import numpy as np 

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    return [l.strip("\n") for l in lines]

def day1(data):
    data = [int(d) for d in data]
    c = 0
    for i in range(1,len(data)):
        if data[i-1] < data[i]: c += 1
    print(f"Day 1 part 1: {c}")

    three_sums = list()
    for i in range(len(data)-2):
        three_sums.append( 
            data[i] + data[i+1] + data[i+2]
         )
    c = 0 
    for i in range(1,len(three_sums)):
        if three_sums[i-1] < three_sums[i]: c += 1
    print(f"Day 1 part 2: {c}")


def day2(data):
    instr = [d.split(' ') for d in data]
    x,y = 0,0
    for dir,num in instr:
        num = int(num)
        if dir == "forward":
            x += num 
        elif dir == "up":
            y -= num 
        elif dir == "down":
            y += num
    print(f"Day 2 part 1: {x*y}")

    x,y,aim = 0,0,0
    for dir, num in instr:
        num = int(num)
        if dir == "forward":
            x += num 
            y += (aim * num)
        if dir == "up":
            aim -= num 
        if dir == "down":
            aim += num 
    print(f"Day 2 part 2: {x*y}")


def day3(data):
    data = [list(d) for d in data]
    X = np.array(data,dtype=int)
    gamma, epsilon = str(), str()
    for j in range(X.shape[1]):
        vals,counts = np.unique(X[:,j],return_counts=True)
        if counts[0] > counts[1]:
            gamma += str(vals[0])
            epsilon += str(vals[1])
        else:
            gamma += str(vals[1])
            epsilon += str(vals[0])
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    print(f"Day 3 part 1: {gamma*epsilon}")

    oxy = X.copy() 
    lifesup = X.copy()
    for j in range(X.shape[1]):
        vals, counts = np.unique(oxy[:,j],return_counts=True)
        ind = vals[0] if counts[0] > counts[1] else vals[1]
        if counts[0] == counts[1]: ind = 1
        oxy = oxy[oxy[:,j] == ind]

        if lifesup.shape[0] > 1:
            vals, counts = np.unique(lifesup[:,j],return_counts=True)
            ind = vals[0] if counts[0] < counts[1] else vals[1]
            if counts[0] == counts[1]: ind = 0
            lifesup = lifesup[lifesup[:,j] == ind ] 

    oxy = int("".join([str(c) for c in oxy[0]]), 2)
    lifesup = int("".join([str(c) for c in lifesup[0]]), 2)
    print(f"Day 3 part 2: {oxy*lifesup}")
        

class Bingo():
    def __init__(self,board):
        self.marked = {(ind,i): 0 for ind in ['row','col']
                         for i in range(len(board))}
        self.board = dict()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.board[board[i][j]] = (i,j)
        
    def mark_board(self,num):
        if num in self.board:
            row, col = self.board[num]
            self.marked[ ('row', row) ] += 1
            self.marked[ ('col', col) ] += 1
            if self.marked[ ('row', row) ] == 5 or self.marked[ ('col', col) ] == 5:
                return True 
        return False
    
    def calc_score(self,num,called):
        unmarked_tot = sum( [key for key in self.board.keys() if key not in called] )
        return num * unmarked_tot

def day4(data):
    nums = [int(d) for d in data[0].split(",")]
    bingos = list()
    for i in range(2,len(data),6):
        parsed = [[int(d) for d in data[j].strip().replace("  ", " ").split(" ")] for j in range(i,i+5)]
        bingos.append(Bingo(parsed))
    
    called = set()
    for num in nums:
        called.add(num)
        is_won = [b.mark_board(num) for b in bingos]
        ind = [i for i, x in enumerate(is_won) if x]
        if ind:
            res = bingos[ind[0]].calc_score(num,called)
            print(f"Day 4 part 1: {res}")
            break
    
    #Part 2
    bingos = list()
    for i in range(2,len(data),6):
        parsed = [[int(d) for d in data[j].strip().replace("  ", " ").split(" ")] for j in range(i,i+5)]
        bingos.append(Bingo(parsed))
    called,has_won = set(), set()
    for num in nums:
        called.add(num)
        is_won = [b.mark_board(num) for b in bingos]
        ind = [i for i,x in enumerate(is_won) if x]
        new_win = [i for i in ind if i not in has_won]
        for x in ind: 
            has_won.add(x) 
        if len(has_won) == len(bingos):
            res = bingos[new_win[0]].calc_score(num,called)
            print(f"Day 4 part 2: {res}")
            break

class Point():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    

class Line():
    def __init__(self,start, end):
        self.start = start 
        self.end = end
        self.horiz = self.start.x == self.end.x
    
    def fill_grid(self,grid):
        if self.horiz:
            for j in range(self.start.y, self.end.y+1):
                grid[self.start.x,j] += 1
        else: 
            for i in range(self.start.x, self.end.x + 1):
                grid[i,self.start.y] += 1


def day5(data):
    for row in data:
        x1,y1,x2,y2 = row[0], row[2], row[7], row[9]
        print(x1) 


if __name__ == "__main__":
    input = read_input("day1.txt")
    day1(input)

    input = read_input("day2.txt")
    day2(input)

    input = read_input('day3.txt')
    day3(input)

    input = read_input('day4.txt')
    day4(input)

    input = read_input('day5.txt')
    day5(input)