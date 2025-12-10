#!/usr/bin/env python

# Imports
import fileinput

# Constants
BATTERY_NUMBER = 12
SKIP_ITEM = 1


def main():
    joltage_sum = 0
    for line in fileinput.input():
        line = line.strip()
        bank_number = 0
        current_index = 0
        for i in reversed(range(BATTERY_NUMBER)):
            current_selection = (
                "0" * current_index + line[current_index : -i if i != 0 else None]
            )
            digit = max(current_selection)
            current_index = current_selection.index(digit) + SKIP_ITEM
            bank_number = bank_number * 10 + int(digit)
        joltage_sum += bank_number
    print(joltage_sum)


if __name__ == "__main__":
    main()
