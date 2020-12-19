# Imports
from python.util.Utility import read_rows, binary_to_decimal

# Day 5 of Advent of Code

# Data for Day 5
file = '../../data/5.input'

# Retrieve Data from File
data = read_rows(file)

# Part One
maximum_seat_id = 0

for entry in data:
    row_section = entry[:-3:].replace('F', '0').replace('B', '1')
    seat_section = entry[-3::].replace('L', '0').replace('R', '1')

    row = binary_to_decimal(row_section)
    seat = binary_to_decimal(seat_section)

    seat_id = (row * 8) + seat

    if seat_id > maximum_seat_id:
        maximum_seat_id = seat_id

# Day 5 Part 1
print('Day 5 Part 1: ' + str(maximum_seat_id))
