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


def decimal_to_binary(decimal, padded_length):
    binary_value = []

    while decimal > 0:
        remainder = decimal % 2
        decimal = int(decimal / 2)
        binary_value.insert(0, str(remainder))

    binary_value = pad_to_size(binary_value, padded_length)

    return binary_value


def pad_to_size(value, padded_length):
    padded_value = value

    while len(value) < padded_length:
        padded_value.insert(0, '0')

    return ''.join(value)
