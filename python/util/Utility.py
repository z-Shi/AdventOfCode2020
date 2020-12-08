# Utility Functions


def read_integers(filename):
    with open(filename) as f:
        return [int(line) for line in f]


def read_rows(filename):
    with open(filename) as f:
        return [line.strip() for line in f]
