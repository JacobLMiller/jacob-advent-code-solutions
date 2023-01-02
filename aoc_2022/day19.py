import numpy as np 

def read_input(path):
    myfile = open(path, 'r')
    lines = myfile.readlines()
    myfile.close()
    lines = [l.strip("\n") for l in lines]
    return lines

class Blueprint():
    def __init__(self, id,ore_cost, clay_cost, obs_c1, obs_c2, geo_c1, geo_c2): 
        self.id = id
        self.ore = ore_cost
        self.clay = clay_cost
        self.obs1 = obs_c1
        self.obs2 = obs_c2
        self.g1 = geo_c1
        self.g2 = geo_c2

        self.ore_count = 1 
        self.clay_count = 0 
        self.obs_count = 0 
        self.geo_count = 0

#Blueprint 1: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 2 ore and 10 obsidian.
def parse(line):
    l = line.replace("Blueprint ", "")
    l = l.replace(": Each ore robot costs ", ",")
    l = l.replace(" ore. Each clay robot costs ", ",")
    l = l.replace(" ore. Each obsidian robot costs ", ",")
    l = l.replace(" ore and ", ",")
    l = l.replace(" clay. Each geode robot costs ", ",")
    l = l.replace(" ore and ", ",")
    l = l.replace(" obsidian.", "")

    # return [int(d) for d in l.split(",")][1:]
    return [int(d) for d in l.split(",")]

def update_bots(bots, oretype):
    if oretype == "ore":
        bots["ore"] += 1
    elif oretype == "clay":
        bots["clay"] += 1
    elif oretype == "obsidian":
        bots["obsidian"] += 1
    elif oretype == "geode":
        bots["geode"] += 1
    return bots

def update_ores(bots,ores,costs,build):
    if build:
        if build == "geode":
            ores['ore'] -= costs[build][0]
            ores['obsidian'] -= costs[build][1]
        elif build == "obsidian":
            ores['ore'] -= costs[build][0]
            ores['clay'] -= costs[build][1]
        else: ores[build] -= costs[build]
    for oretype in bots:
        ores[oretype] += bots[oretype]
    return ores

from functools import cache

costs = {
    'ore': 4,
    'clay': 2,
    'obsidian': (3,14),
    'geode': (2,7)
}

#Too expensive, search space too large
def F(t, bots, ores, cache):
    if t <= 0: return ores[3]
    print(t)

    print ((t, *bots, *ores))
    if (t,*bots, *ores) in cache: 
        return cache[(t,*bots,*ores)]

    ore_b,clay_b,obs_b,geo_b = bots 
    ore_n, clay_n, obs_n, geo_n = ores

    if ore_b >= 15: return geo_n
    if clay_n > 50: return geo_n
    #case 1, create ore bot
    c1,c2,c3,c4,c5 = geo_n,geo_n,geo_n,geo_n,geo_n
    if ore_n >= costs['ore']:
        c1 = F(t-1,
            (ore_b + 1, clay_b, obs_b, geo_b),
            ((ore_n - costs['ore']) + ore_b, clay_n + clay_b, obs_n + obs_b, geo_n + geo_b),
            cache)
    #case 2, create clay bot
    if ore_n >= costs['clay']:
        c2 = F(t-1,
            (ore_b, clay_b + 1, obs_b, geo_b),
            ((ore_n - costs['clay']) + ore_b, clay_n + clay_b, obs_n + obs_b, geo_n + geo_b),
            cache )
    #case 3, create obsidian bot 
    if ore_n >= costs['obsidian'][0] and clay_n >= costs['obsidian'][1]:
        c3 = F(t-1,
            (ore_b, clay_b, obs_b + 1, geo_b),
            ((ore_n - costs['obsidian'][0]) + ore_b, (clay_n - costs['obsidian'][1]) + clay_b, obs_n + obs_b, geo_n + geo_b),
            cache)
    #case 4, create geode bot 
    if ore_n >= costs['geode'][0] and obs_n >= costs['geode'][1]:
        c4 = F(t-1,
            (ore_b, clay_b, obs_b, geo_b + 1),
            ((ore_n - costs['geode'][0]) + ore_b, clay_n + clay_b, (obs_n - costs['geode'][1]) + obs_b, geo_n + geo_b),
            cache)
    #Case 5, build no robots
    c5 = F(t-1, 
        (ore_b,clay_b,obs_b,geo_b), 
        (ore_n + ore_b, clay_n + clay_b, obs_n + obs_b, geo_n + geo_b),
        cache)

    
    cache[(t,*bots, *ores)] = max([c1,c2,c3,c4,c5])
    return max([c1,c2,c3,c4,c5])
    
from collections import namedtuple 

State = namedtuple('State', ['ore_b', 'clay_b', 'obs_b', 'geo_b',
                            'ore_n', 'clay_n', 'obs_n', 'geo_n',
                            't']
                    )


def heuristic(S):
    return 10000*S.geo_b + 1000 * S.geo_n + 100*S.obs_n + 10*S.clay_n + S.ore_n

def dp_for(time,costs,num_keep=10000):

    ore_c, clay_c, obs_c, geo_c = costs

    Q = [ State(1,0,0,0,0,0,0,0,0)]
    states = set()

    best_geo = 0


    max_c = max(*obs_c, *geo_c, ore_c,clay_c)
    depth = 0

    while Q:
        S = Q.pop()

        best_geo = max(best_geo, S.geo_n)

        if S.t >= time:
            continue

        if S.t > depth:
            Q.sort(key=heuristic,reverse=True)
            Q = Q[:num_keep]
            # if len(Q) > 0:
            #     print(Q[0])
            depth = S.t
        
        #Memoization 
        if S in states:
            continue 
        states.add(S)
        # if S.t == 18:
        #     print(S)
        # if S.geo_b >= 1:
        #     print(S)
        # print(S.t)
        # print(S)
        if len(states) % 1000000 == 0:
            print(f"Time left: {S.t}, best so far: {best_geo}, Size of states: {len(states)}")

        #Either make an ore bot:
        if S.ore_n >= ore_c:
            Q.insert(0,S._replace(
             ore_b=S.ore_b+1,
             ore_n=S.ore_n + S.ore_b - ore_c,
             clay_n=S.clay_n + S.clay_b,
             obs_n = S.obs_n + S.obs_b,
             geo_n = S.geo_n + S.geo_b,
             t=S.t+1))
        #Or a clay bot:
        if S.ore_n >= clay_c:
           Q.insert(0,S._replace(
             clay_b=S.clay_b+1,
             ore_n=S.ore_n + S.ore_b - clay_c,
             clay_n=S.clay_n + S.clay_b,
             obs_n = S.obs_n + S.obs_b,
             geo_n = S.geo_n + S.geo_b,
             t=S.t+1))      
        #Or an obs bot:
        if S.ore_n >= obs_c[0] and S.clay_n >= obs_c[1]:
           Q.insert(0,S._replace(
             obs_b=S.obs_b+1,
             ore_n=S.ore_n + S.ore_b - obs_c[0],
             clay_n=S.clay_n + S.clay_b - obs_c[1],
             obs_n = S.obs_n + S.obs_b,
             geo_n = S.geo_n + S.geo_b,
             t=S.t+1))         
        #Or hopefully a geo bot:
        if S.ore_n >= geo_c[0] and S.obs_n >= geo_c[1]:
           Q.insert(0,S._replace(
             geo_b=S.geo_b+1,
             ore_n=S.ore_n + S.ore_b - geo_c[0],
             clay_n=S.clay_n + S.clay_b,
             obs_n = S.obs_n + S.obs_b - geo_c[1],
             geo_n = S.geo_n + S.geo_b,
             t=S.t+1))          
        #We can also do nothing 
        Q.insert(0,S._replace(
            ore_n=S.ore_n + S.ore_b,
            clay_n=S.clay_n + S.clay_b,
            obs_n = S.obs_n + S.obs_b,
            geo_n = S.geo_n + S.geo_b,
            t=S.t+1))   

    return best_geo




def day19(data):
    B1 = parse(data[0])

    counts = {
        'ore': 1,
        'clay': 0,
        'obsidian': 0,
        'geode': 0
    }

    costs = {
        'ore': 2,
        'clay': 3,
        'obsidian': (3,8),
        'geode': (3,12)
    }

    bots = {
        'ore': 1,
        'clay': 0,
        'obsidian': 0,
        'geode': 0
    }

    m = dp_for(24, (4,2,(3,14), (2,7)))
    # m = F(24, (1,0,0,0), (0,0,0,0), dict())
    print(m)
    m = dp_for(24, (2,3, (3,8), (3,12)))
    print(m)

    V = 0 
    for i,row in enumerate(data):
        B = parse(row)
        print(f"Working on Blueprint {i+1}")
        num, ore_c, clay_c, obs_c1, obs_c2, geo_c1, geo_c2 = B 
        costs = (ore_c, clay_c, (obs_c1, obs_c2), (geo_c1, geo_c2)) 
        best = dp_for(24, costs)
        V += (best*(i+1))
    print(f"Day 19 part 1: {V}")

    #Part 2 

def day19_2(data):

    V = 1 
    for i, row in enumerate(data[:3]):
        B = parse(row)
        print(f"Working on Blueprint {i+1}")
        num, ore_c, clay_c, obs_c1, obs_c2, geo_c1, geo_c2 = B 
        costs = (ore_c, clay_c, (obs_c1, obs_c2), (geo_c1, geo_c2)) 
        best = dp_for(32, costs,9000)
        V *= best
    print(f"Day 19 part 2: {V}")


if __name__ == "__main__":
    input = read_input("day19.txt")
    #day19(input)
    day19_2(input)