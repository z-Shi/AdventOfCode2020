# Imports
from python.util.Utility import read_rows
import copy

# Day 8 of Advent of Code

# Data for Day 8
file = '../../data/8.input'

# Retrieve Data from File
data = read_rows(file)


# Common Functions
def execute(instructions, instruction_index, seen_instruction_indexes):
    accumulator_value = 0
    done_processing = False

    while instruction_index < len(instructions):
        instruction = instructions[instruction_index]

        if instruction_index in seen_instruction_indexes:
            break
        else:
            seen_instruction_indexes.append(instruction_index)

        if instruction['operation'] == operation_acc:
            if instruction['direction'] == '+':
                accumulator_value += instruction['value']
            elif instruction['direction'] == '-':
                accumulator_value -= instruction['value']

            instruction_index += 1
        elif instruction['operation'] == operation_nop:
            instruction_index += 1
        elif instruction['operation'] == operation_jmp:
            if instruction['direction'] == '+':
                instruction_index += instruction['value']
            elif instruction['direction'] == '-':
                instruction_index -= instruction['value']

    if instruction_index == len(instructions):
        done_processing = True

    return accumulator_value, done_processing


# Part One
operation_acc = 'acc'
operation_jmp = 'jmp'
operation_nop = 'nop'

original_instructions = []
for entry in data:
    parts = entry.split(' ')
    operation = parts[0]
    direction = parts[1][0]
    value = parts[1][1:].rstrip()
    original_instructions.append({
        'operation': operation,
        'direction': direction,
        'value': int(value)
    })

accumulator, processing_completed = execute(original_instructions, 0, [])

# Day 8 Part 1
print(f'Day 8 Part 1: {accumulator}')


# Part Two Functions
def part_two(instructions):
    for index in range(0, len(instructions)):
        working_instructions = copy.deepcopy(instructions)

        if working_instructions[index]['operation'] != operation_acc:
            if working_instructions[index]['operation'] == operation_jmp:
                working_instructions[index].update({'operation': operation_nop})
            else:
                working_instructions[index].update({'operation': operation_jmp})

            val, successful_completion = execute(working_instructions, 0, [])

            if successful_completion:
                global accumulator
                accumulator = val
                return


# Part Two
part_two(original_instructions)

# Day 8 Part 2
print(f'Day 8 Part 2: {accumulator}')
