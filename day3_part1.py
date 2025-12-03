#!/usr/bin/env python

# Imports
import fileinput

# Constants
CUT_LAST_ITEM = -1
SKIP_ITEM = 1


def main():
    joltage_sum = 0
    for line in fileinput.input():
        line = line.strip()
        tens_digit = max(line[:CUT_LAST_ITEM])
        tens_digit_index = line.index(tens_digit)
        units_digit = max(line[tens_digit_index + SKIP_ITEM :])
        joltage_sum += int(tens_digit) * 10 + int(units_digit)
    print(joltage_sum)


if __name__ == "__main__":
    main()
