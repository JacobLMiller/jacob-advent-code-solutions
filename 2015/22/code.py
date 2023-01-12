# Advent of code Year 2015 Day 22 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

from collections import namedtuple 

Player = namedtuple("Player", ("hp","mana"))
Boss = namedtuple("Boss", ("hp", "dmg"))



costs = {
    "MM": 53, 
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229
}


class Spell():
    def __init__(self,cost,dmg,heal,effect,timer):
        self.cost = cost 
        self.dmg = dmg 
        self.heal = heal 
        self.effect = effect
        self.timer = timer 
    
    def cast(self,gamestate,p2=False):
        #state = Player, Boss, effects, mana
        P,B, effects, tot_mana = gamestate

        if P.mana < self.cost:
            return gamestate 

        #Spell should not be active
        if self.effect > 0: 
            if effects[self.effect-1] > 0:
                return gamestate
            else:
                effects = list(effects)
                effects[self.effect-1] = self.timer
                effects = tuple(effects)
        
        P = P._replace(hp=P.hp+self.heal, mana=P.mana-self.cost)
        B = B._replace(hp=B.hp-self.dmg)
        tot_mana = tot_mana + self.cost

        return (P,B,effects,tot_mana)


def do_effect(gamestate):
    P,B, effects, tot_mana = gamestate

    out = tuple([max(0,x-1) for x in effects])

    if effects[1] > 0:
        B = B._replace(hp=B.hp-3)
    if effects[2] > 0:
        P = P._replace(mana=P.mana+101)
    
    return (P,B,out,tot_mana)

def do_boss(gamestate):
    P,B,effects,tot_mana = do_effect(gamestate)

    dmg = B.dmg
    if effects[0] > 0:
        dmg -= 7
    
    P = P._replace(hp=P.hp - dmg)

    return (P,B,effects,tot_mana)
    

spells = (
    Spell(53,4,0,0,0),
    Spell(73, 2, 2, 0, 0),
    Spell(113,0,0,1,6),
    Spell(173, 0, 0, 2, 6),
    Spell(229,0,0,3,5)
)
        
def part2():
    P = Player(50,500)
    B = Boss(71,10)
    effects = (0,0,0) #Shield, Poison, Recharge

    s = (P,B,effects,0)

    Q = [s]
    cache = {s}
    min_mana = 5e9

    while len(Q) > 0:
        p = Q.pop()

        P,B,e,t = p 
        P = P._replace(hp = P.hp - 1)
        if P.hp <= 0:
            continue 
        p = (P,B,e,t)
        p = do_effect(p)

        for spell in spells:
            next = spell.cast(p)
            if next == p:
                continue
            next = do_boss(next)


            P,B,_,tot_mana = next
            if B.hp <= 0:
                min_mana = min(min_mana, tot_mana)
                continue 

            if next not in cache and P.hp >= 0 and tot_mana <= min_mana and P.mana > 53:
                cache.add(next)
                Q.append(next)
    return min_mana



def part1():
    P = Player(50,500)
    B = Boss(71,10)    
    effects = (0,0,0) #Shield, Poison, Recharge

    s = (P,B,effects,0)

    Q = [s]
    cache = {s}
    min_mana = 5e9

    while len(Q) > 0:
        p = Q.pop()

        p = do_effect(p)

        for spell in spells:
            next = spell.cast(p)
            if next == p:
                continue
            next = do_boss(next)


            P,B,_,tot_mana = next
            if B.hp <= 0:
                min_mana = min(min_mana, tot_mana)
                continue 

            if next not in cache and P.hp >= 0 and tot_mana <= min_mana and P.mana > 53:
                cache.add(next)
                Q.append(next)
    return min_mana

p1 = part1()
p2 = part2()

print("Part One : "+ str(p1))



print("Part Two : "+ str(p2))