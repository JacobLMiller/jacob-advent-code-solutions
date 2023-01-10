# Advent of code Year 2015 Day 22 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

#Hp, ac, mana
P = (50, 0, 500)
#Hp, dmg
B = 71

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
    
    def cast(spell,gamestate):
        pass
    
    


print("Part One : "+ str(None))



print("Part Two : "+ str(None))