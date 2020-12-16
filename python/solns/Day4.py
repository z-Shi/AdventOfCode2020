# Imports
from python.util.Utility import read_rows
import re

# Day 4 of Advent of Code

# Data for Day 4
file = '../../data/4.input'

# Retrieve Data from File
data = read_rows(file)
required_props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


# Part One

# Read Passports
passports = []
pass_index = 0

for entry in data:
    if pass_index >= len(passports):
        passports.append({})

    if entry != '':
        properties = entry.split(' ')

        for prop in properties:
            key = prop.split(':')[0]
            value = prop.split(':')[1]

            passports[pass_index][key] = value
    else:
        pass_index += 1

# Count Number of Valid Passports
valid_passports = 0

for passport in passports:
    valid = True

    for field in required_props:
        if field not in passport:
            valid = False

    if valid:
        valid_passports += 1

# Day 4 Part 1
print("Day 4 Part 1: " + str(valid_passports))


# Part Two
def validate_passport(some_passport):
    is_valid = True

    if len(some_passport) < len(required_props):
        return False

    for p in required_props:
        if p not in some_passport:
            return False

    if not (1920 <= int(some_passport['byr']) <= 2002):
        is_valid = False
    if not (2010 <= int(some_passport['iyr']) <= 2020):
        is_valid = False
    if not (2020 <= int(some_passport['eyr']) <= 2030):
        is_valid = False

    if 'cm' in some_passport['hgt'] and not (150 <= int(some_passport['hgt'][:-2]) <= 193):
        is_valid = False
    elif 'in' in some_passport['hgt'] and not (59 <= int(some_passport['hgt'][:-2]) <= 76):
        is_valid = False

    if 'cm' not in some_passport['hgt'] and 'in' not in some_passport['hgt']:
        is_valid = False

    if some_passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        is_valid = False
    if re.match(r'^#[0-9a-f]{6}$', some_passport['hcl']) is None:
        is_valid = False
    if re.match(r'^\d{9}$', some_passport['pid']) is None:
        is_valid = False

    return is_valid


valid_passports = 0

for passport in passports:
    valid = validate_passport(passport)

    if valid:
        valid_passports += 1

# Day 4 Part 2
print("Day 4 Part 2: " + str(valid_passports))
