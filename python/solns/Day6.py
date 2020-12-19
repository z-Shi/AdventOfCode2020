# Imports
from python.util.Utility import read_rows

# Day 6 of Advent of Code

# Data for Day 6
file = '../../data/6.input'

# Retrieve Data from File
data = read_rows(file)

# Part One
index = 0
entries = []
no_of_questions = 0

for entry in data:
    if index >= len(entries):
        entries.append('')

    if entry != '':
        entries[index] += entry
    else:
        index += 1

for entry in entries:
    question_count = len(set(entry))
    no_of_questions += question_count

# Day 6 Part 1
print('Day 6 Part 1: ' + str(no_of_questions))

