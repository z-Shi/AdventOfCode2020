# Imports
from itertools import combinations
from python.util.Utility import read_integers


# Day 1 of Advent of Code


# Data for Day 1
file = '../../data/1.input'
goal = 2020


# Retrieve Data from File
data = read_integers(file)
entries = ()


# Part One


# Find Correct Entries
for pair in combinations(data, 2):
    if sum(pair) == goal:
        entries = pair

# Output Result for Part 1
result = entries[0] * entries[1]
print("Day 1 Part 1: " + str(result))


# Part Two


# Find Correct Entries
for triple in combinations(data, 3):
    if sum(triple) == goal:
        entries = triple


# Output Result for Part 2
result = entries[0] * entries[1] * entries[2]
print("Day 1 Part 2: " + str(result))
