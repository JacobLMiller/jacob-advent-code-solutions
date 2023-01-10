# Advent of code Year 2015 Day 21 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    boss_stats = [d.replace("Hit Points: ", "").replace("Damage: ", "").replace("Armor: ", "")
        for d in input]
    boss_stats = [int(d) for d in boss_stats]

weapons = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

armor = """Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

rings = """Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

weapons = weapons.split("\n")[1:]
armor = armor.split("\n")[1:]
rings = rings.split("\n")[1:]

class Entity():
    def __init__(self,hp,dmg,ac):
        self.base_hp = hp
        self.hp = hp 
        self.base_dmg = dmg 
        self.base_ac = ac
        self.dmg = dmg 
        self.ac = ac
        self.invest = 0
    
    def equip(self,item):
        self.dmg += item.dmg
        self.ac += item.ac
        self.invest += item.gp
    
    def unequip(self):
        self.dmg = self.base_dmg
        self.ac = self.base_ac
        self.invest = 0
        self.hp = self.base_hp

    def reset(self):
        self.hp = self.base_hp

class Item(Entity):
    def __init__(self,gp,dmg,ac):
        self.gp = gp 
        self.dmg = dmg 
        self.ac = ac

def Fight(Player,Boss):
    # print(f"Fight with Player {(Player.hp, Player.dmg, Player.ac)} and Boss {(Boss.hp, Boss.dmg, Boss.ac)}")
    while True:
        Boss.hp -= max(1,(Player.dmg - Boss.ac))
        if Boss.hp <= 0: return True 
        Player.hp -= max(1,(Boss.dmg - Player.ac))
        if Player.hp <= 0: return False



Boss = Entity(*boss_stats)
Player = Entity(100, 0, 0)

weapons = [",".join(w.split()).split(",")[1:] for w in weapons]
armor = [",".join(w.split()).split(",")[1:] for w in armor]
rings = [",".join(w.split()).split(",")[2:] for w in rings]

weapons = [Item(int(gp), int(dmg), int(ac)) for gp,dmg,ac in weapons]
armor = [Item(0,0,0)] + [Item(int(gp), int(dmg), int(ac)) for gp,dmg,ac in armor]
rings = [Item(0,0,0)] + [Item(int(gp), int(dmg), int(ac)) for gp,dmg,ac in rings]

import itertools
win_costs = list()
lose_costs = list()
#Choose 1 weapon
for w in weapons:
    #Choose up to 1 armor
    for a in armor:
        #Choose up to 2 rings 
        for r1 in rings:
            for r2 in rings:
                if r1 == r2: continue
                Player.equip(w)
                Player.equip(a)
                Player.equip(r1)
                Player.equip(r2)
                if Fight(Player,Boss):
                    win_costs.append(Player.invest)
                else:
                    if Player.invest == 208:
                        print(Player.dmg, Player.ac)
                    lose_costs.append(Player.invest)
                Player.unequip()
                Boss.reset()

print("Part One : "+ str(min(win_costs)))


print("Part Two : "+ str(max(lose_costs)))