#!/usr/bin/env python

# Imports
import fileinput
from itertools import takewhile

# Constants
EMPTY_LINE = "\n"
RANGE = "-"
INCLUSIVE = 1


def main():
    puzzle = fileinput.input()
    product_ranges = {}
    new_product_ranges = {
        (int(start), int(end))
        for start, end in (
            line.strip().split(RANGE)
            for line in takewhile(lambda line: line != EMPTY_LINE, puzzle)
        )
    }
    while new_product_ranges != product_ranges:
        product_ranges = new_product_ranges
        range_dict = {
            product_range: [
                overlapping_range
                for overlapping_range in product_ranges
                if product_range[0] <= overlapping_range[0] <= product_range[1]
                or overlapping_range[0] <= product_range[0] <= overlapping_range[1]
            ]
            for product_range in product_ranges
        }
        new_product_ranges = {
            (
                min(overlapping_range[0] for overlapping_range in overlapping_ranges),
                max(overlapping_range[1] for overlapping_range in overlapping_ranges),
            )
            for product_range, overlapping_ranges in range_dict.items()
        }
    unique_ids = sum(end + INCLUSIVE - start for start, end in product_ranges)
    print(unique_ids)


if __name__ == "__main__":
    main()
