#!/usr/bin/env python

# Imports
import fileinput
import itertools
from functools import reduce

# Constants
ON = "#"
TUPLE = ","
TUPLE_DELIMITERS = "()"
LIST_DELIMITERS = "[]"


def infinite_combinations_with_replacement(lst):
    for length in itertools.count(start=1):
        yield from itertools.combinations_with_replacement(lst, length)


def find_num_presses(indicator_lights, buttons):
    indicator_lights = {
        position for position, light in enumerate(indicator_lights) if light == ON
    }
    possible_combinations = infinite_combinations_with_replacement(buttons)
    presses_final_state = {}
    while presses_final_state != indicator_lights:
        guess = next(possible_combinations)
        presses_final_state = reduce(set.symmetric_difference, guess)
    return len(guess)


def parse_row(row):
    indicator_lights, *other_input = row.strip().split()
    buttons = [
        {int(member) for member in item.strip(TUPLE_DELIMITERS).split(TUPLE)}
        for item in other_input[:-1]
    ]
    return (indicator_lights.strip(LIST_DELIMITERS), buttons)


def main():
    puzzle = (parse_row(row) for row in fileinput.input())
    sum_presses = sum(
        find_num_presses(indicator_lights, buttons)
        for indicator_lights, buttons in puzzle
    )
    print(sum_presses)


if __name__ == "__main__":
    main()
