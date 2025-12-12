#!/usr/bin/env python

# Imports
import fileinput

# Constants
SIGN = -1


def transpose(matrix):
    "Swap the rows and columns of a 2-D matrix."
    return zip(*matrix, strict=True)


def main():
    puzzle = [row.strip().split() for row in fileinput.input()]
    problems = (row[SIGN].join(row[:SIGN]) for row in transpose(puzzle))
    print(sum(map(eval, problems)))


if __name__ == "__main__":
    main()
