#!/usr/bin/python

with open("$FILE", 'r') as f:
  data = [a.strip() for a in f.readlines()]

oxygen = data.copy()
co2 = data.copy()

# Get oxygen
for i in range(len(oxygen[0])):
    column = [int(d[i]) for d in oxygen]

    if sum(column) < (len(oxygen) / 2):
        oxygen = [val for val in oxygen if val[i] == '0']
    elif sum(column) >= (len(oxygen) / 2):
        oxygen = [val for val in oxygen if val[i] == '1']
    
    if len(oxygen) == 1:
        break

# Get co2
for i in range(len(co2[0])):
    column = [int(d[i]) for d in co2]

    if sum(column) < (len(co2) / 2):
        co2 = [val for val in co2 if val[i] == '1']
    elif sum(column) >= (len(co2) / 2):
        co2 = [val for val in co2 if val[i] == '0']
    
    if len(co2) == 1:
        break

oxygen = oxygen[0]
co2 = co2[0]


print(int(oxygen, 2) * int(co2, 2))
