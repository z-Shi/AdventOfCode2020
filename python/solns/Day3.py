# Imports
from python.util.Utility import read_rows


# Day 3 of Advent of Code

# Data for Day 3
file = '../../data/3.input'

# Retrieve Data from File
data = read_rows(file)

# Part One
row = 0
col = 0

no_of_cols = len(data[0])
no_of_rows = len(data)

cols_step = 3
rows_step = 1

trees = 0

while row < no_of_rows:
    if (col + cols_step) >= no_of_cols:
        col = (col + cols_step) - no_of_cols

    if data[row][col] == '#':
        trees += 1

    row += rows_step
    col += cols_step

print('trees: ' + str(trees))
