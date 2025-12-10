#!/usr/bin/env python

# Imports
import fileinput
from itertools import combinations
import shapely


# Constants
TUPLE = ","


def area_calc(coordinates):
    a, b = coordinates
    ax, ay = a
    bx, by = b
    width = abs(ax - bx) + 1
    height = abs(ay - by) + 1
    return width * height


def main():
    red_tiles = [
        (int(x), int(y))
        for x, y in (row.strip().split(TUPLE) for row in fileinput.input())
    ]
    polygon = shapely.Polygon(red_tiles)
    possible_rectangles = possible_rectangles = (
        (point1, point2)
        for point1, point2 in combinations(red_tiles, 2)
        if polygon.contains(shapely.box(*point1, *point2))
    )
    largest_rectangle = max(possible_rectangles, key=area_calc)
    print(area_calc(largest_rectangle))


if __name__ == "__main__":
    main()
