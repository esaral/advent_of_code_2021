#!/usr/bin/python

with open("$FILE", 'r') as f:
    data = [a.strip() for a in f.readlines()]

vals = []

for d in data:
    signals, outputs = d.split(' | ')
    signals = signals.split()
    outputs = outputs.split()

    for o in outputs:
        if len(o) in [2, 3, 4, 7]:
            vals.append(o)

print(len(vals))
