#!/usr/bin/env python

# Imports
import fileinput
import numpy as np

# Constants
SIGN = -1


def main():
    puzzle = [row.strip().split() for row in fileinput.input()]
    rearranged_puzzle = np.array(puzzle).T
    problems = (row[SIGN].join(row[:SIGN]) for row in rearranged_puzzle)
    results = (eval(problem) for problem in problems)
    print(sum(results))


if __name__ == "__main__":
    main()
