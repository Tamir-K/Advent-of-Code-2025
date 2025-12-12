#!/usr/bin/env python

# Imports
import fileinput
from itertools import takewhile

# Constants
FIRST_ROW = 0
SIGN = -1


def transpose(matrix):
    "Swap the rows and columns of a 2-D matrix."
    return zip(*matrix, strict=True)


def main():
    puzzle = [list(row.rstrip("\n")) for row in fileinput.input()]
    rearranged_puzzle = transpose(puzzle)
    total_sum = 0
    while problem := list(
        takewhile(lambda row: any(char.strip() for char in row), rearranged_puzzle)
    ):
        sign = problem[FIRST_ROW][SIGN]
        problem = sign.join("".join(row[:SIGN]) for row in problem)
        total_sum += eval(problem)
    print(total_sum)


if __name__ == "__main__":
    main()
