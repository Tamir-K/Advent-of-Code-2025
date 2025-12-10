#!/usr/bin/env python

# Imports
import fileinput
import numpy as np
from scipy.optimize import linprog

# Constants
ON = "#"
TUPLE = ","
TUPLE_DELIMITERS = "()"
SET_DLIMITERS = "{}"


def find_minimal_coefficients(joltage_counters, buttons):
    buttons = [
        [int(num in button) for num in range(len(joltage_counters))]
        for button in buttons
    ]
    A = np.array(buttons).T
    b = np.array(joltage_counters)
    res = linprog(
        c=np.ones(len(buttons)),
        A_eq=A,
        b_eq=b,
        method="highs",
        integrality=[1] * len(buttons),
    )
    return res.x if res.success else None


def parse_row(row):
    indicator_lights, *other_input = row.strip().split()
    buttons = [
        [int(member) for member in item.strip(TUPLE_DELIMITERS).split(TUPLE)]
        for item in other_input[:-1]
    ]
    joltage_counters = [
        int(member) for member in other_input[-1].strip(SET_DLIMITERS).split(TUPLE)
    ]
    return (buttons, joltage_counters)


def main():
    puzzle = (parse_row(row) for row in fileinput.input())
    sum_presses = sum(
        sum(find_minimal_coefficients(joltage_counters, buttons))
        for buttons, joltage_counters in puzzle
    )
    print(sum_presses)


if __name__ == "__main__":
    main()
