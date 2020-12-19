# Imports
from python.util.Utility import read_rows, binary_to_decimal

# Day 5 of Advent of Code

# Data for Day 5
file = '../../data/5.input'

# Retrieve Data from File
data = read_rows(file)

# Part One
maximum_seat_id = 0
seat_ids = []

for entry in data:
    row_section = entry[:-3:].replace('F', '0').replace('B', '1')
    seat_section = entry[-3::].replace('L', '0').replace('R', '1')

    row = binary_to_decimal(row_section)
    seat = binary_to_decimal(seat_section)

    seat_id = (row * 8) + seat
    seat_ids.append(seat_id)

    if seat_id > maximum_seat_id:
        maximum_seat_id = seat_id

# Day 5 Part 1
print('Day 5 Part 1: ' + str(maximum_seat_id))

# Part Two
available_seat_id = [seat for seat in range(min(seat_ids), max(seat_ids)) if seat not in seat_ids][0]

# Day 5 Part 2
print('Day 5 Part 2: ' + str(available_seat_id))
