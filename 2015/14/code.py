# Advent of code Year 2015 Day 14 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    input = [d.replace(" can fly ", ",")
            .replace(" km/s for ", ",")
            .replace(" seconds, but then must rest for ", ",")
            .replace(" seconds.", "")
            for d in input]

class Reindeer():
    def __init__(self, name, spd, run_time, rest_time):
        self.name = name
        self.spd = spd 
        self.r_time = run_time
        self.w_time = rest_time
        self.dist = 0
        self.resting = False
        self.period = 0

    def sim(self, n):
        dist = 0 
        while n > 0:
            if self.r_time <= n:
                dist += (self.spd * self.r_time)
                n -= (self.r_time + self.w_time)
            else:
                dist += (self.spd * n)
                n -= n
        return dist
    
    def sim2(self):
        if self.resting:
            self.period += 1 
        elif not self.resting:
            self.dist += self.spd 
            self.period += 1
        
        if self.resting and self.period == self.w_time:
            self.period = 0
            self.resting = False 
        elif not self.resting and self.period == self.r_time:
            self.period = 0
            self.resting = True 

        return self.dist
            


reindeers = list()
for row in input:
    name, spd, r_time, w_time = row.split(",")
    R = Reindeer(name,int(spd),int(r_time),int(w_time))
    reindeers.append(R)

ans = max(R.sim(2503) for R in reindeers)

print("Part One : "+ str(ans))

import numpy as np
points = [0 for _ in reindeers]
for _ in range(2503):
    win = np.argmax([R.sim2() for R in reindeers])
    points[win] += 1

print("Part Two : "+ str(max(points)))