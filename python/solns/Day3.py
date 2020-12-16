# Imports
from python.util.Utility import read_rows


# Day 3 of Advent of Code

# Data for Day 3
file = '../../data/3.input'

# Retrieve Data from File
data = read_rows(file)
no_of_cols = len(data[0])
no_of_rows = len(data)


# Functions for Task(s)
def count_trees(column_step, row_step):
    no_of_trees = 0
    row = 0
    col = 0

    while row < no_of_rows:
        if col >= no_of_cols:
            col = col % no_of_cols

        if data[row][col] == '#':
            no_of_trees += 1

        row += row_step
        col += column_step

    return no_of_trees


# Part One
cols_step = 3
rows_step = 1

trees = count_trees(cols_step, rows_step)

print('Day 3 Part 1: ' + str(trees))


# Part Two
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_entries = []

for slope in slopes:
    trees = count_trees(slope[0], slope[1])
    tree_entries.append(trees)

result = 1

for entry in tree_entries:
    result *= entry

print('Day 3 Part 2: ' + str(result))
