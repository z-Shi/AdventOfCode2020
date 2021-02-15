# Imports
from python.util.Utility import read_rows, decimal_to_binary, binary_to_decimal
import re

# Day 14 of Advent of Code

# Data for Day 14
file = '../../data/14.input'
ASSIGNMENT_SEPARATOR = ' = '
DEFAULT_BIT_MASK = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


# Retrieve Data from File
data = read_rows(file)


# The initialization program (your puzzle input) can either update the
# bitmask or write a value to memory.
# Values and memory addresses are both 36-bit unsigned integers.
# For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would write the
# value 11 to memory address 8.
# The bitmask is always given as a string of 36 bits, written with the
# most significant bit (representing 2^35) on the left and the least
# significant bit (2^0, that is, the 1s bit) on the right. The current
# bitmask is applied to values immediately before they are written to
# memory: a 0 or 1 overwrites the corresponding bit in the value,
# while an X leaves the bit in the value unchanged.
# For example, consider the following program:
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# This program starts by specifying a bitmask (mask = ....). The
# mask it specifies will overwrite two bits in every written value:
# the 2s bit is overwritten with 0, and the 64s bit is overwritten
# with 1.
# The program then attempts to write the value 11 to memory address
# 8. By expanding everything out to individual bits, the mask is
# applied as follows:
# value:  000000000000000000000000000000001011  (decimal 11)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001001001  (decimal 73)
# So, because of the mask, the value 73 is written to memory address
# 8 instead. Then, the program tries to write 101 to address 7:
# value:  000000000000000000000000000001100101  (decimal 101)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001100101  (decimal 101)
# This time, the mask has no effect, as the bits it overwrote were
# already the values the mask tried to set. Finally, the program
# tries to write 0 to address 8:
# value:  000000000000000000000000000000000000  (decimal 0)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001000000  (decimal 64)
# 64 is written to address 8 instead, overwriting the value that was
# there previously.
# Execute the initialization program. What is the sum of all values
# left in memory after it completes? (Do not truncate the sum to 36
# bits.)


# Part One Functions
def execute_commands(cmds, mask):
    bit_mask = mask
    mem = {}

    for cmd in cmds:
        parts = cmd.split(ASSIGNMENT_SEPARATOR)

        if len(parts[1]) == 36:
            bit_mask = parts[1]
        else:
            location = int(parts[0].split('[')[1][:-1])
            value = int(parts[1])
            value = update_value(value, bit_mask)
            mem[location] = value

    return mem


def apply_bit_mask(binary_val, mask):
    masked_val = []

    for index in range(0, 36):
        if mask[index] == 'X':
            masked_val.append(binary_val[index])
        else:
            masked_val.append(mask[index])

    return ''.join(masked_val)


def update_value(val, mask):
    binary_value = decimal_to_binary(val, 36)
    masked_value = apply_bit_mask(binary_value, mask)
    return binary_to_decimal(masked_value)


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
