#!/usr/bin/env python

# Imports
import fileinput
from itertools import takewhile

# Constants
EMPTY_LINE = "\n"
RANGE = "-"


def main():
    puzzle = fileinput.input()
    product_ranges = [
        (int(start), int(end))
        for start, end in (
            line.strip().split(RANGE)
            for line in takewhile(lambda line: line != EMPTY_LINE, puzzle)
        )
    ]
    product_ids = (int(line.strip()) for line in puzzle)
    fresh_products = sum(
        any(start <= id <= end for start, end in product_ranges) for id in product_ids
    )
    print(fresh_products)


if __name__ == "__main__":
    main()
