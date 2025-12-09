#!/usr/bin/env python

# Imports
import fileinput
from itertools import combinations


# Constants
TUPLE = ","


def area_calc(coordinates):
    a, b = coordinates
    ax, ay = a
    bx, by = b
    width = ax - bx + 1
    height = ay - by + 1
    return abs(width * height)


def main():
    red_tiles = (
        (int(x), int(y))
        for x, y in (row.strip().split(TUPLE) for row in fileinput.input())
    )
    possible_rectangles = combinations(red_tiles, 2)
    largest_rectangle = max(possible_rectangles, key=area_calc)
    print(area_calc(largest_rectangle))


if __name__ == "__main__":
    main()
