# Imports
from python.util.Utility import read_rows

# Day 15 of Advent of Code

# Data for Day 15
file = '../../data/15.input'

# Retrieve Data from File
data = read_rows(file)
last_occurrence_table = {}


# Part One Functions
def generate_sequence(sequence, end_step_number):
    for _ in range(len(sequence), end_step_number):
        *history, consider = sequence
        if consider in history:
            sequence.append(list(reversed(history)).index(consider) + 1)
        else:
            sequence.append(0)

    return sequence[-1]


def parse_input(raw_data):
    return [int(x) for x in raw_data[0].split(',')]


def part_one(raw_data):
    sequence = parse_input(raw_data)
    return generate_sequence(sequence, 2020)


# Part One
result = part_one(data)

# Day 15 Part 1
print(f'Day 15 Part 1: {result}')


# Part Two Functions
def generate_sequence_part_two(sequence, end_step_number):
    dict_data = {value: key for key, value in enumerate(sequence[:-1])}
    consider = sequence[-1]
    value = 0

    for index in range(len(sequence), end_step_number):
        if consider in dict_data:
            value = (index - 1) - dict_data[consider]
        else:
            value = 0

        dict_data[consider] = index - 1
        consider = value

    return value


def parse_input_part_two(raw_data):
    return [int(x) for x in raw_data[0].split(',')]


def part_two(raw_data):
    sequence = parse_input_part_two(raw_data)
    return generate_sequence_part_two(sequence, 30000000)


# Part Two
result = part_two(data)

# Day 15 Part 2
print(f'Day 15 Part 2: {result}')
