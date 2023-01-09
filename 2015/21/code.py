# Advent of code Year 2015 Day 21 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    boss_stats = [d.replace("Hit Points: ", "").replace("Damage: ", "").replace("Armor: ", "")
        for d in input]
    boss_stats = [int(d) for d in boss_stats]

shop = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

print(shop)

class Entity():
    def __init__(self,hp,dmg,ac):
        self.hp = hp 
        self.dmg = dmg 
        self.ac = ac

print("Part One : "+ str(None))



print("Part Two : "+ str(None))