#!/usr/bin/python

with open("$FILE", 'r') as f:
  data = [a.strip() for a in f.readlines()]

gamma = ''
epsilon = ''

column_len = len(data[0])

for i in range(column_len):
    column = [int(d[i]) for d in data]
    if sum(column) < len(data) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
