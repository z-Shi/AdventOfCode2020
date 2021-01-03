# Imports
from python.util.Utility import read_rows
import math

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
X = 'X'
Y = 'Y'

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


def calculate_manhattan_distance(horizontal, vertical):
    return abs(horizontal) + abs(vertical)


# Part One
instructions = parse_instructions(data)
position = execute_instructions(instructions)
distance = calculate_manhattan_distance(position[WEST] - position[EAST], position[NORTH] - position[SOUTH])

# Day 12 Part 1
print(f'Day 12 Part 1: {distance}')


# Part Two Functions
def rotate(location, angle_in_radians):
    location_x, location_y = location

    rotated_x = round((math.cos(angle_in_radians) * location_x) - (math.sin(angle_in_radians) * location_y))
    rotated_y = round((math.sin(angle_in_radians) * location_x) + (math.cos(angle_in_radians) * location_y))

    return int(rotated_x), int(rotated_y)


def execute_instructions_part_two(base_instructions):
    current_position = {X: 0, Y: 0}
    waypoint_position = {X: 10, Y: 1}

    for instruction in base_instructions:
        command = instruction[0]
        value = instruction[1]

        if command == COMMAND_NORTH:
            waypoint_position[Y] += value
        elif command == COMMAND_SOUTH:
            waypoint_position[Y] -= value
        elif command == COMMAND_EAST:
            waypoint_position[X] += value
        elif command == COMMAND_WEST:
            waypoint_position[X] -= value
        elif command == COMMAND_FORWARD:
            current_position[X] += waypoint_position[X] * value
            current_position[Y] += waypoint_position[Y] * value
        elif command == COMMAND_RIGHT or command == COMMAND_LEFT:
            if command == COMMAND_RIGHT:
                value = -value

            waypoint_position[X], waypoint_position[Y] = rotate((waypoint_position[X], waypoint_position[Y]),
                                                                math.radians(value))

    return current_position


# Part Two
instructions = parse_instructions(data)
position = execute_instructions_part_two(instructions)
distance = calculate_manhattan_distance(position[X], position[Y])

# Day 12 Part 2
print(f'Day 12 Part 2: {distance}')
