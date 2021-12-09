#!/usr/bin/python

with open("$FILE", 'r') as f:
    data = [a.strip() for a in f.readlines()][0]

positions = sorted([int(a) for a in data.split(',')])

# ======
# part1
# ======
def part_1():
    median = positions[len(positions)//2]
    part1 = sum([abs(p-median) for p in positions])

    return part1

# ======
# part2
# ======
def get_fuel(position):
    fuel = 0
    for p in positions:
        distance = abs(p - position)
        fuel += sum(range(distance + 1))

    return fuel

def part_2():
    # Calculate mean for both floor and ceiling and take the lower result
    mean1 = round(sum(positions) / len(positions))
    fuel1 = get_fuel(mean1)

    mean2 = sum(positions) // len(positions)
    fuel2 = get_fuel(mean2)

    return min(fuel1, fuel2)

print(part_1())
print(part_2())
