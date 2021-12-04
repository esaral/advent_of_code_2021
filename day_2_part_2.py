#!/usr/bin/python

with open("$FILE", 'r') as f:
  data = [a.strip() for a in f.readlines()]

pos = 0
depth = 0
aim = 0

for d in data:
    direction, value = d.split()
    value = int(value)
    
    if direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    elif direction == 'forward':
        pos += value
        depth += aim * value

print(pos * depth)
