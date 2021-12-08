#!/usr/bin/python

with open("$FILE", 'r') as f:
  data = [a.strip() for a in f.readlines()]

points = [(a, b) for a, b in [set(d.split(' -> ')) for d in data]]

vents = {}

for p1, p2 in points:
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                if (x, y) in vents:
                    vents[(x, y)] += 1
                else:
                    vents[(x, y)] = 1

print(len([vent for vent, n in vents.items() if n >= 2]))
