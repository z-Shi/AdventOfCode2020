# Utility Functions


def read_integers(filename):
    with open(filename) as f:
        return [int(line) for line in f]


def read_rows(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


def binary_to_decimal(binary):
    decimal_value = 0
    base = 1

    for index in range(len(binary) - 1, -1, -1):
        if binary[index] == '1':
            decimal_value += base
        base *= 2

    return decimal_value
