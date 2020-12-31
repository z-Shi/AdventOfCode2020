# Imports
from python.util.Utility import read_integers

# Day 9 of Advent of Code

# Data for Day 9
file = '../../data/9.input'

# Retrieve Data from File
data = read_integers(file)


# Part One Functions
def part_one(numbers, preamble):
    index = 0
    valid = False

    for first_number in numbers:
        numbers.pop(index)

        for second_number in numbers:
            if first_number + second_number == preamble:
                valid = True

        numbers.insert(index, first_number)
        index += 1

    return valid


def process(numbers, preamble):
    start = 0
    end = preamble

    while end < len(numbers):
        number = numbers[end]
        stack = numbers[start:end]

        if not part_one(stack, number):
            return number
        else:
            start += 1
            end += 1


# Part One
value = process(data, 25)

# Day 9 Part 1
print(f'Day 9 Part 1: {value}')


# Part Two Functions
def part_two(numbers, target):
    for left_index, val in enumerate(numbers):
        nums = [val]
        total = val
        right_index = left_index + 1

        while total < target:
            total += numbers[right_index]
            nums.append(numbers[right_index])

            if total == target:
                return sorted(nums)[0] + sorted(nums)[-1]

            right_index += 1


# Part Two
value = part_two(data, process(data, 25))

# Day 9 Part 2
print(f'Day 9 Part 2: {value}')
