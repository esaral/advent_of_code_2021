#!/usr/bin/python

with open("$FILE", 'r') as f:
  data = [a.strip() for a in f.readlines()]

pos = 0
depth = 0

for d in data:
    direction, value = d.split()
    value = int(value)
    
    if direction == 'forward':
        pos += value
    elif direction == 'down':
        depth += value
    elif direction == 'up':
        depth -= value

print(pos * depth)
