# Imports
from python.util.Utility import read_rows, decimal_to_binary, binary_to_decimal
import copy

# Day 14 of Advent of Code

# Data for Day 14
file = '../../data/14.input'
ASSIGNMENT_SEPARATOR = ' = '
DEFAULT_BIT_MASK = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
DEFAULT_BIT_MASK_PART_TWO = '000000000000000000000000000000000000'
BIT_MASK_LENGTH = 36


# Retrieve Data from File
data = read_rows(file)


# Part One Functions
def execute_commands(cmds, mask):
    bit_mask = mask
    mem = {}

    for cmd in cmds:
        parts = cmd.split(ASSIGNMENT_SEPARATOR)

        if len(parts[1]) == BIT_MASK_LENGTH:
            bit_mask = parts[1]
        else:
            location = int(parts[0].split('[')[1][:-1])
            value = int(parts[1])
            value = update_value(value, bit_mask)
            mem[location] = value

    return mem


def update_value(val, mask):
    binary_value = decimal_to_binary(val, BIT_MASK_LENGTH)
    masked_value = apply_bit_mask(binary_value, mask)
    return binary_to_decimal(masked_value)


def apply_bit_mask(binary_val, mask):
    masked_val = []

    for index in range(0, BIT_MASK_LENGTH):
        if mask[index] == 'X':
            masked_val.append(binary_val[index])
        else:
            masked_val.append(mask[index])

    return ''.join(masked_val)


def part_one():
    memory = execute_commands(data, DEFAULT_BIT_MASK)
    sum_value = 0

    for entry in memory.values():
        sum_value += entry

    return sum_value


# Part One
result = part_one()

# Day 14 Part 1
print(f'Day 14 Part 1: {result}')


# Part Two Functions
def execute_commands_part_two(cmds, mask):
    bit_mask = mask
    mem = {}

    for cmd in cmds:
        parts = cmd.split(ASSIGNMENT_SEPARATOR)

        if len(parts[1]) == BIT_MASK_LENGTH:
            bit_mask = parts[1]
        else:
            original_location = int(parts[0].split('[')[1][:-1])
            value = int(parts[1])
            masked_location = apply_bit_mask_part_two(decimal_to_binary(original_location, BIT_MASK_LENGTH), bit_mask)
            fluctuating_addresses_list = gather_fluctuating_address_list(masked_location)

            for fluctuating_address in fluctuating_addresses_list:
                location = binary_to_decimal(fluctuating_address)
                mem[location] = value

    return mem


def apply_bit_mask_part_two(binary_val, mask):
    masked_val = []

    for index in range(0, BIT_MASK_LENGTH):
        if mask[index] == '0':
            masked_val.append(binary_val[index])
        elif mask[index] == '1':
            masked_val.append('1')
        else:
            masked_val.append('X')

    return ''.join(masked_val)


def gather_fluctuating_address_list(masked_address):
    fluctuating_bit_count = masked_address.count('X')
    fluctuating_address_list = []

    for combination_value in range(0, (2 ** fluctuating_bit_count)):
        current_address = copy.deepcopy(masked_address)
        current_bits = decimal_to_binary(combination_value, fluctuating_bit_count)

        for index in range(0, len(current_bits)):
            current_address = current_address.replace('X', current_bits[index], 1)

        fluctuating_address_list.append(current_address)

    return fluctuating_address_list


def part_two():
    memory = execute_commands_part_two(data, DEFAULT_BIT_MASK_PART_TWO)
    sum_value = 0

    for entry in memory.values():
        sum_value += entry

    return sum_value


# Part Two
result = part_two()

# Day 14 Part 2
print(f'Day 14 Part 2: {result}')
