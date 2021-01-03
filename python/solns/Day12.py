# Imports
from python.util.Utility import read_rows

# Day 12 of Advent of Code

# Data for Day 12
file = '../../data/12.input'
NORTH_DEGREES = 0
EAST_DEGREES = 90
SOUTH_DEGREES = 180
WEST_DEGREES = 270
NORTH, COMMAND_NORTH = 'N', 'N'
EAST, COMMAND_EAST = 'E', 'E'
SOUTH, COMMAND_SOUTH = 'S', 'S'
WEST, COMMAND_WEST = 'W', 'W'
COMMAND_FORWARD = 'F'
COMMAND_LEFT = 'L'
COMMAND_RIGHT = 'R'

# Retrieve Data from File
data = read_rows(file)


# Part One Functions
def parse_instructions(raw_data):
    base_instructions = []

    for entry in raw_data:
        command = entry[0]
        value = int(entry[1:])
        base_instructions.append((command, value))

    return base_instructions


def execute_instructions(base_instructions):
    current_position = {NORTH: 0, EAST: 0, SOUTH: 0, WEST: 0}
    direction = EAST

    for instruction in base_instructions:
        command = instruction[0]
        value = instruction[1]

        if command == COMMAND_NORTH or command == COMMAND_EAST or command == COMMAND_WEST or command == COMMAND_SOUTH:
            current_position[command] += value
        elif command == COMMAND_FORWARD:
            current_position[direction] += value
        else:
            modification = int(value / 90)

            if command == COMMAND_LEFT:
                directions = [EAST, NORTH, WEST, SOUTH]
                new_direction = (directions.index(direction) + modification) % len(directions)
                direction = directions[new_direction]
            elif command == COMMAND_RIGHT:
                directions = [EAST, SOUTH, WEST, NORTH]
                new_direction = (directions.index(direction) + modification) % len(directions)
                direction = directions[new_direction]

    return current_position


def calculate_manhattan_distance(current_position):
    return abs(current_position[WEST] - current_position[EAST]) + abs(current_position[NORTH] - current_position[SOUTH])


# Part One
instructions = parse_instructions(data)
position = execute_instructions(instructions)
distance = calculate_manhattan_distance(position)

# Day 12 Part 1
print(f'Day 12 Part 1: {distance}')
