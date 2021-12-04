#!/usr/bin/python

with open("$FILE", 'r') as f:
  data = [a.strip() for a in f.readlines()]


greater = []

i = 0

while i < len(data)-3:
    if report[i] < report[i+3]:
        greater.append(report[i])
    i += 1


print(len(greater))
