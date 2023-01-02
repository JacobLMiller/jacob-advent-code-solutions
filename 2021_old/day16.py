

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

def parse_num(bin):
    cont, i, num, = 1, 1, ""
    while cont: 
        num += bin[i:i+4]
        cont = int(bin[i-1])
        i += 5
    return int(num, 2)

def read_hex(bin):
    print(bin)
    version = int(bin[:3],2)
    p_type = int(bin[3:6],2)
    if p_type == 4: 
        return (version, p_type, parse_num(bin[6:]))
    
    l_type = int(bin[6])
    if l_type == 0: 
        L = int(bin[7:7+15], 2)
        return {"version": version, "p_type": p_type, "child": read_hex(bin[7+15:7+15+L])}
    elif l_type == 1:
        L = int(bin[7:7+11], 2)
        
    print(L)

def day16(data):
    bin = "{0:08b}".format(int(data[0],16))
    h = read_hex(bin)
    print(h)


if __name__ == "__main__":
    input = read_input("day16.txt")
    day16(input)
