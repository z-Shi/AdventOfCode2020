# Imports
from python.util.Utility import read_rows

# Day 11 of Advent of Code

# Data for Day 11
file = '../../data/11.input'

# Retrieve Data from File
data = read_rows(file)


# Part One Functions
def parse_grid(rows):
    grid = []

    for row in rows:
        grid_row = [letter for letter in row]
        grid.append(grid_row)

    return grid


def count_occupied_adjacent(grid, row_index, col_index):
    adjacent_indexes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    num_of_rows = len(grid)
    num_of_cols = len(grid[0])
    occupied_count = 0

    for adjacent_index in adjacent_indexes:
        row = row_index + adjacent_index[0]
        col = col_index + adjacent_index[1]

        if 0 <= row < num_of_rows and 0 <= col < num_of_cols and grid[row][col] == '#':
            occupied_count += 1

    return occupied_count


def apply_rules(grid, threshold=4, two=False):
    num_of_rows = len(grid)
    num_of_cols = len(grid[0])
    modified = False
    new_grid = [['' for entry in range(num_of_cols)] for row in range(num_of_rows)]

    for row_index in range(num_of_rows):
        for col_index in range(num_of_cols):
            if grid[row_index][col_index] == '.':
                new_grid[row_index][col_index] = '.'
            else:
                if two:
                    occupied = count_occupied_directional(grid, row_index, col_index)
                else:
                    occupied = count_occupied_adjacent(grid, row_index, col_index)

                if grid[row_index][col_index] == 'L' and occupied == 0:
                    new_grid[row_index][col_index] = '#'
                    modified = True
                elif grid[row_index][col_index] == '#' and occupied >= threshold:
                    new_grid[row_index][col_index] = 'L'
                    modified = True
                else:
                    new_grid[row_index][col_index] = grid[row_index][col_index]

    return new_grid, modified


def count_occupied(grid):
    occupied_count = 0

    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            if grid[row_index][col_index] == '#':
                occupied_count += 1

    return occupied_count


def part_one(grid):
    modified = True

    while modified:
        grid, modified = apply_rules(grid)

    return grid


# Part One
seat_grid = parse_grid(data)
result_grid = part_one(seat_grid)
no_of_occupied_seats = count_occupied(result_grid)

# Day 11 Part 1
print(f'Day 11 Part 1: {no_of_occupied_seats}')


# Part Two Functions
def count_occupied_directional(grid, row_index, col_index):
    adjacent_indexes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    num_of_rows = len(grid)
    num_of_cols = len(grid[0])
    occupied_count = 0

    for adjacent_index in adjacent_indexes:
        row = row_index + adjacent_index[0]
        col = col_index + adjacent_index[1]

        while 0 <= row < num_of_rows and 0 <= col < num_of_cols:
            if grid[row][col] == 'L':
                break
            elif grid[row][col] == '#':
                occupied_count += 1
                break

            row += adjacent_index[0]
            col += adjacent_index[1]

    return occupied_count


def part_two(grid):
    modified = True

    while modified:
        grid, modified = apply_rules(grid, 5, True)

    return grid


# Part Two
seat_grid = parse_grid(data)
result_grid = part_two(seat_grid)
no_of_occupied_seats = count_occupied(result_grid)

# Day 11 Part 2
print(f'Day 11 Part 2: {no_of_occupied_seats}')
