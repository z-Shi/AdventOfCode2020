# Imports
from python.util.Utility import read_rows

# Day 16 of Advent of Code

# Data for Day 16
file = '../../data/16.input'

# Retrieve Data from File
data = read_rows(file)
colon_sep = ': '
or_sep = ' or '
dash_sep = '-'
comma_sep = ','
departure = 'departure'


# Part One Functions
def parse_data(raw_data):
    rules = raw_data[:20]
    ticket = raw_data[22:23]
    tickets_nearby = raw_data[25:]

    return rules, ticket, tickets_nearby


def parse_raw_rules(raw_rules):
    rules = {}

    for rule in raw_rules:
        name_plus_rule = rule.split(colon_sep)
        split_rule = name_plus_rule[1].split(or_sep)
        name = name_plus_rule[0]
        condition_one = split_rule[0].split(dash_sep)
        condition_two = split_rule[1].split(dash_sep)
        rules[name] = [int(condition_one[0]), int(condition_one[1]), int(condition_two[0]), int(condition_two[1])]

    return rules


def parse_raw_ticket(raw_ticket):
    return [int(x) for x in raw_ticket[0].split(comma_sep)]


def parse_raw_tickets_nearby(raw_tickets_nearby):
    return [[int(x) for x in entry.split(comma_sep)] for entry in raw_tickets_nearby]


def check_if_valid_field(rules, field):
    return any([(rule[0] <= field <= rule[1]) or (rule[2] <= field <= rule[3]) for rule in rules.values()])


def part_one(raw_data):
    raw_rules, raw_ticket, raw_tickets_nearby = parse_data(raw_data)
    rules = parse_raw_rules(raw_rules)
    tickets_nearby = parse_raw_tickets_nearby(raw_tickets_nearby)
    error_rate = sum([field for nearby_ticket in tickets_nearby
                      for field in nearby_ticket if not check_if_valid_field(rules, field)])

    return error_rate


# Part One
result = part_one(data)

# Day 16 Part 1
print(f'Day 16 Part 1: {result}')


# Part Two Functions
def part_two(raw_data):
    raw_rules, raw_ticket, raw_tickets_nearby = parse_data(raw_data)
    rules = parse_raw_rules(raw_rules)
    ticket = parse_raw_ticket(raw_ticket)
    tickets_nearby = parse_raw_tickets_nearby(raw_tickets_nearby)

    valid_tickets = [nearby_ticket for nearby_ticket in tickets_nearby
                     if all([check_if_valid_field(rules, field) for field in nearby_ticket])]

    possible_rows = {}
    for name, rule in rules.items():
        possible_rows[name] = [index for index in range(len(rules))
                               if all([check_if_valid_field({name: rule}, valid_ticket[index])
                                       for valid_ticket in valid_tickets])]

    specific_rows = {}
    for name, possible_row in sorted(possible_rows.items(), key=lambda possibility: len(possibility[1])):
        row_index = [index for index in possible_row if index not in specific_rows]
        specific_rows[row_index[0]] = name

    departure_fields = [field for index, field in enumerate(ticket) if departure in specific_rows[index]]

    departure_result = 1
    for departure_field in departure_fields:
        departure_result *= departure_field

    return departure_result


# Part Two
result = part_two(data)

# Day 16 Part 2
print(f'Day 16 Part 2: {result}')
