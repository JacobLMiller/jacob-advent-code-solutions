def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

s_to_d = {
    '=': -2, 
    '-': -1, 
    '0': 0,
    '1': 1,
    '2': 2
}

d_to_s = {
    -2: '=', 
    -1: '-',
    0: '0', 
    1: '1', 
    2: '2' 
}


"""
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       15            1=0
       20            1-0
     2022         1=11-2
    12345        1-0---0
314159265  1121-1110-1=0
"""

base_map = {
    1: "1",
    10: "20",
    100: "1-00",
    1000: "2=000",
    2: "2", 
    3: "1=",
    4: "1-",
    5: "10",
    6: "11",
    7: "12",
    8: "2=",
    9: "2-",
}

def b5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return s

def add_base_5(num,add = 2):
    n = len(num)
    carry = 0
    for k in range(n):
        tmp = int(num[n-k-1]) + add  + carry
        if tmp >= 5:
            carry += 1
    

def SNAFU_to_dec(snafu):
    n = len(snafu)

    dec = 0
    for p in range(len(snafu)):
        dec += pow(5,p)*s_to_d[snafu[n-p-1]]
    return dec 

snafumap = {
    -2: "=",
    -1: "-", 
    0: "0",
    1: "1",
    2: "2"
}

import math
def dec_to_snafu(dec):
    s = ""
    while dec != 0:
        s += snafumap[( dec + 2 ) % 5 - 2]
        dec = (dec - ((dec + 2) % 5 - 2)) // 5

    return s[::-1]

def day25(data):
    p1 = sum([SNAFU_to_dec(d) for d in data])
    print(dec_to_snafu(p1))

if __name__ == "__main__":
    input = read_input("day25.txt")
    day25(input)