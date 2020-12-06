# Utility Functions


def read_integers(filename):
    with open(filename) as f:
        return [int(line) for line in f]
