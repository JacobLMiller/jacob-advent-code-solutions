def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

def expression(s):
    _,t1,e,t2 = s.split(" ")
    return [e, t1, t2]

def parse(data):
    T = dict()
    for row in data:
        mon, info = row.split(":")
        try:
            d = int(info)
        except:
            d = expression(info)
        T[mon] = d 
    return T

def perform_expression(exp):
    e,t1,t2 = exp 
    if e == "+":
        return t1+t2 
    elif e == "-":
        return t1-t2 
    elif e == "*":
        return t1*t2 
    elif e == "/":
        return t1//t2

def day21(data):
    Tree = parse(data)

    while type(Tree['root']) != int :
        for key,item in Tree.items():
            if type(item) == int: continue 
            for i in [1,2]:
                if type(item[i]) == str:
                    if type(Tree[item[i]]) == int:
                        item[i] = Tree[item[i]]
            if type(item[1]) == int and type(item[2]) == int:
                Tree[key] = int(perform_expression(item))
        
    print(Tree['root'])

def p_item(item):
    if type(item) == int:
        return item 
    return "{} {} {}".format(item[1], item[0], item[2])

def traverse(T,root='root'):
    print(f"{root} = {p_item(T[root])}")
    if type(T[root]) == list: 
        if type(T[root][1]) != int:
            traverse(T,T[root][1])
        if type(T[root][2]) != int:
            traverse(T,T[root][2])

def backtrack(T,root, val):
    if root == "humn": return val

    e,t1,t2 = T[root]
    if e in ["=", "+", "*"]:
        t1,t2 = (t1,t2) if type(t1) == int else (t2,t1)

    if e == "=": return backtrack(T,t2,t1)
    elif e == "+": return backtrack(T,t2,val-t1)
    elif e == "*": return backtrack(T,t2, val//t1)


    if e == "-": 
        #5 = 6 - x
        if type(t1) == int: return backtrack(T, t2, -1*(val-t1))
        #5 = x - 4
        return backtrack(T,t1,val+t2)
    elif e == "/": 
        #5 = 6 / x
        if type(t1) == int: return backtrack(T,t2, t1//val)
        #5 = x / 6    
        return backtrack(T,t1,val*t2)

def day21_2(data):
    Tree = parse(data)
    for _ in range(100):
        for key,item in Tree.items():
            if type(item) == int: continue 
            for i in [1,2]:
                if type(item[i]) == str and item[i] != "humn":
                    if type(Tree[item[i]]) == int:
                        item[i] = Tree[item[i]]
            if type(item[1]) == int and type(item[2]) == int:
                Tree[key] = int(perform_expression(item))
    traverse(Tree)

    Tree['root'][0] = "="

    print(backtrack(Tree,'root',0))




if __name__ == "__main__":
    input = read_input("day21.txt")
    day21(input)
    day21_2(input)