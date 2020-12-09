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
    if col >= no_of_cols:
        col = col % no_of_cols

    if data[row][col] == '#':
        trees += 1

    row += rows_step
    col += cols_step

print('Day 3 Part 1: ' + str(trees))


# Part Two
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_entries = []

for slope in slopes:
    tree_count = 0
    cols_step = slope[0]
    rows_step = slope[1]
    row = 0
    col = 0

    while row < no_of_rows:
        if col >= no_of_cols:
            col = col % no_of_cols

        if data[row][col] == '#':
            tree_count += 1

        row += rows_step
        col += cols_step

    tree_entries.append(tree_count)

result = 1

for tree_count in tree_entries:
    result *= tree_count

print('Day 3 Part 2: ' + str(result))
