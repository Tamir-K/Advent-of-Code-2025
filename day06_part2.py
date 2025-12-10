#!/usr/bin/env python

# Imports
import fileinput
import numpy as np
import re

# Constants
SIGN = -1
SPACE = " "
ADDITION = "+"


def main():
    puzzle = [re.split(r"", row.rstrip("\n")) for row in fileinput.input()]
    rearranged_puzzle = np.array(puzzle).T

    sign = None
    result = 0
    total_sum = 0
    for row in rearranged_puzzle:
        if not (np.any(row != SPACE) & np.any(row)):
            total_sum += result
            sign = None
            result = 0
        elif sign is None:
            sign = row[SIGN]
            result = int("".join(row[:SIGN]))
        else:
            result = (
                result + int("".join(row))
                if sign == ADDITION
                else result * int("".join(row))
            )
    print(total_sum)


if __name__ == "__main__":
    main()
