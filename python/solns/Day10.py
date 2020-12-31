# Imports
from python.util.Utility import read_integers

# Day 10 of Advent of Code

# Data for Day 10
file = '../../data/10.input'

# Retrieve Data from File
data = read_integers(file)


# Part One Functions
def part_one(numbers):
    outlet_rating = 0
    count_ones = 0
    count_twos = 0
    count_threes = 0
    maximum = max(data) + 3
    data.append(maximum)

    while True:
        if (outlet_rating + 1) in numbers:
            count_ones += 1
            outlet_rating += 1
        elif (outlet_rating + 2) in numbers:
            count_twos += 1
            outlet_rating += 2
        elif (outlet_rating + 3) in numbers:
            count_threes += 1
            outlet_rating += 3
        else:
            return count_ones * count_threes


# Part One
value = part_one(data)

# Day 10 Part 1
print(f'Day 10 Part 1: {value}')


# Part Two Functions
def part_two(numbers):
    solution = {0: 1}

    for number in sorted(numbers):
        solution[number] = 0
        if number - 1 in solution:
            solution[number] += solution[number - 1]
        if number - 2 in solution:
            solution[number] += solution[number - 2]
        if number - 3 in solution:
            solution[number] += solution[number - 3]

    return solution[max(numbers)]


# Part Two
value = part_two(data)

# Day 10 Part 2
print(f'Day 10 Part 2: {value}')
