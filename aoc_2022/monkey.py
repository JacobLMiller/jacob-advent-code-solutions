from aoc_2022 import Monkey
##Copy monkey attributes
def get_monkeys():
    M0 = Monkey([93,98],
        op = lambda x: x * 17 , 
        test = lambda x: True if x % 19 == 0 else False,
        true=5,
        false=3,
        ind = 0
    )
    M1 = Monkey([95,72,98,82,86],
        op = lambda x: x + 5 , 
        test = lambda x: True if x % 13 == 0 else False,
        true=7,
        false=6,
        ind = 1
    )
    M2 = Monkey([85, 62, 82, 86, 70, 65, 83, 76],
        op = lambda x: x + 8 , 
        test = lambda x: True if x % 5 == 0 else False,
        true=3,
        false=0,
        ind = 2
    )
    M3 = Monkey([86, 70, 71, 56],
        op = lambda x: x + 1 , 
        test = lambda x: True if x % 7 == 0 else False,
        true=4,
        false=5,
        ind = 3
    )   
    M4 = Monkey([77, 71, 86, 52, 81, 67],
        op = lambda x: x + 4 , 
        test = lambda x: True if x % 17 == 0 else False,
        true=1,
        false=6,
        ind = 4
    )   
    M5 = Monkey([89, 87, 60, 78, 54, 77, 98],
        op = lambda x: x * 7 , 
        test = lambda x: True if x % 2 == 0 else False,
        true=1,
        false=4,
        ind = 5
    )       
    M6 = Monkey([69, 65, 63],
        op = lambda x: x + 6 , 
        test = lambda x: True if x % 3 == 0 else False,
        true=7,
        false=2,
        ind = 6
    )   
    M7 = Monkey([89],
        op = lambda x: x * x , 
        test = lambda x: True if x % 11 == 0 else False,
        true=0,
        false=2,
        ind = 7
    )
    return [M0,M1,M2,M3,M4,M5,M6,M7]