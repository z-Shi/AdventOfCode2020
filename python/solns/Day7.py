# Imports
from python.util.Utility import read_rows
import re

# Day 7 of Advent of Code

# Data for Day 7
file = '../../data/7.input'

# Retrieve Data from File
data = read_rows(file)
search_type = 'shiny gold'


# Part One Functions
def count_bags(bags, bag_name):
    bag_count = 0
    chosen_bag = bags[bag_name]

    if len(chosen_bag) == 0:
        return bag_count
    else:
        for sub_bag in chosen_bag:
            if sub_bag['type'] == search_type:
                bag_count += 1
            bag_count += count_bags(bags, sub_bag['type'])

    return bag_count


def part_one(bags):
    bag_count = 0

    for bag_name in bags.keys():
        if count_bags(bags, bag_name) > 0:
            bag_count += 1

    return bag_count


# Part One
bag_rules = {}

for entry in data:
    entry_regex = r'^(\w+ \w+) bags contain (.*)'
    bag_regex = r'([0-9] )*(\w+ \w+) bag'

    outer_bag_and_contents = re.search(entry_regex, entry)
    outer_bag = outer_bag_and_contents[1]
    outer_bag_contents = outer_bag_and_contents[2][:-1]

    contents = re.findall(bag_regex, outer_bag_contents)
    rules = []

    for item in contents:
        if item[1] != 'no other':
            rules.append({
                'count': int(item[0]),
                'type': item[1]
            })

    bag_rules[outer_bag] = rules

bag = 'shiny gold'
count = part_one(bag_rules)

# Day 7 Part 1
print(f'Day 7 Part 1: {count}')


# Part Two Functions
def part_two(bags, bag_name):
    bag_count = 0
    top_level_bag = bags[bag_name]

    if len(top_level_bag) == 0:
        return bag_count
    else:
        for current_bag in top_level_bag:
            current_bag_count = current_bag['count']
            bag_count += current_bag_count
            bags_inside_current_bag_count = part_two(bags, current_bag['type'])
            bag_count += bags_inside_current_bag_count * current_bag_count

    return bag_count


# Part Two
count = part_two(bag_rules, search_type)

# Day 7 Part 2
print(f'Day 7 Part 2: {count}')
