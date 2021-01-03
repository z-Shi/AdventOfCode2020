# Imports
from python.util.Utility import read_rows

# Day 13 of Advent of Code

# Data for Day 13
file = '../../data/13.input'

# Retrieve Data from File
data = read_rows(file)


# Part One Functions
def parse_data(input_data):
    earliest_timestamp = int(input_data[0].strip())
    bus_list = []

    for entry in input_data[1].split(','):
        if entry != 'x':
            bus_list.append(int(entry))

    return earliest_timestamp, bus_list


def find_earliest_departure_time(earliest_timestamp, bus_list):
    departure_time = None
    bus_id = None
    found = False
    time = earliest_timestamp

    while not found:
        for bus in bus_list:
            if time % bus == 0:
                departure_time = time
                bus_id = bus
                found = True

        time += 1

    return departure_time, bus_id


def part_one(earliest_timestamp, timestamp, bus_id):
    time_diff = timestamp - earliest_timestamp
    return bus_id * time_diff


# Part One
earliest_departure_time, buses = parse_data(data)
actual_departure_time, actual_bus = find_earliest_departure_time(earliest_departure_time, buses)
result = part_one(earliest_departure_time, actual_departure_time, actual_bus)

# Day 13 Part 1
print(f'Day 13 Part 1: {result}')


# Part Two Functions
def get_full_bus_list(input_data):
    bus_list = []

    for entry in input_data[1].split(','):
        bus_list.append(entry)

    return bus_list


def part_two(bus_list):
    timestamp, step = 100000000000000, 1
    bus_details = [(int(bus), bus_index) for bus_index, bus in enumerate(bus_list) if bus != 'x']

    for bus_id, offset in bus_details:
        while (timestamp + offset) % bus_id != 0:
            timestamp += step

        step *= bus_id

    return timestamp


# Part Two
buses = get_full_bus_list(data)
result = part_two(buses)

# Day 13 Part 2
print(f'Day 13 Part 2: {result}')
