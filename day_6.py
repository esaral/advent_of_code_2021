#!/usr/bin/python

with open("$FILE", 'r') as f:
    data = [a.strip() for a in f.readlines()][0]

ages = [int(a) for a in data.split(',')]

fish_per_age = {i:ages.count(i) for i in range(9)}

# days = 80  #part1
days = 256   #part2

for _ in range(days):
    spawn = fish_per_age[0]

    for i in range(8):
        fish_per_age[i] = fish_per_age[i+1]
    fish_per_age[6] += spawn
    fish_per_age[8] = spawn

print(sum(fish_per_age.values()))
