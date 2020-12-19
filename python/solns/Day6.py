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

# Part Two
index = 0
entries = []
no_of_questions = 0

for entry in data:
    if index >= len(entries):
        entries.append([])

    if entry != '':
        entries[index].append(entry)
    else:
        index += 1

for entry in entries:
    question_count = 0

    if len(entry) == 0:
        continue
    elif len(entry) == 1:
        question_count = len(set(entry[0]))
    else:
        common_questions = set(entry[0])

        for index in range(1, len(entry)):
            common_questions = common_questions.intersection(set(entry[index]))

        question_count = len(common_questions)

    no_of_questions += question_count

# Day 6 Part 2
print('Day 6 Part 2: ' + str(no_of_questions))
