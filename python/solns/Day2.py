# Imports
from python.util.Utility import read_rows


# Day 2 of Advent of Code

# Data for Day 2
file = '../../data/2.input'

# Retrieve Data from File
data = read_rows(file)

# Part One
valid_passwords = 0

for row in data:
    parts = row.rstrip().split(':')

    condition = parts[0].split(' ')
    password = parts[1]

    occur_conditions = condition[0].split('-')
    min_occurs = int(occur_conditions[0])
    max_occurs = int(occur_conditions[1])
    letter = condition[1]

    no_occurs = password.count(letter)

    if min_occurs <= no_occurs <= max_occurs:
        valid_passwords += 1

print("Day 2 Part 1: " + str(valid_passwords))

# Part Two
valid_passwords = 0

for row in data:
    parts = row.rstrip().split(':')

    condition = parts[0].split(' ')
    password = parts[1].strip()

    split_conditions = condition[0].split('-')
    pos_one = int(split_conditions[0]) - 1
    pos_two = int(split_conditions[1]) - 1
    letter = condition[1]

    if (((password[pos_one] == letter) and (password[pos_two] != letter)) or
            ((password[pos_one] != letter) and (password[pos_two] == letter))):
        valid_passwords += 1

print("Day 2 Part 2: " + str(valid_passwords))
