#!/usr/bin/env python

# Imports
import fileinput
from itertools import takewhile, product

# Constants
AREA_INDICATOR = "x"
SHAPE_ID = 0
SHAPE_FORMAT = 1
SHAPE_FILL = "#"
DELIMITER = ":"
NUM_SHAPES = 6


def parse_shape_defs(puzzle):
    shape_defs = {}
    for _ in range(NUM_SHAPES):
        shape_iterator = list(takewhile(lambda row: row, puzzle))
        shape_defs[int(shape_iterator[SHAPE_ID].strip(DELIMITER))] = [
            (i, j)
            for i, item in enumerate(shape_iterator[SHAPE_FORMAT:])
            for j, char in enumerate(item)
            if char == SHAPE_FILL
        ]
    return shape_defs


def parse_area_def(row):
    area_def, *shapes = row.strip().split()
    return area_def.strip(DELIMITER), [
        position for position, count in enumerate(shapes) for _ in range(int(count))
    ]


def rotate_point(point):
    """Rotate a point 90 degrees clockwise"""
    x, y = point
    return y, -x


def get_all_rotations(points):
    """Generate all four rotations of the given points using yield"""
    current_rotation = points

    for _ in range(4):
        yield current_rotation
        current_rotation = [rotate_point(point) for point in current_rotation]
        min_x = min(x for x, _ in current_rotation)
        min_y = min(y for _, y in current_rotation)
        current_rotation = [(x - min_x, y - min_y) for x, y in current_rotation]


def in_bounding_box(shape, dim1, dim2):
    return all(0 <= x < dim1 and 0 <= y < dim2 for x, y in shape)


def can_fit(area_def, shapes, shape_defs):
    dim1, dim2 = [int(dim) for dim in area_def.split(AREA_INDICATOR)]
    area = dim1 * dim2
    total_size = sum(len(shape_defs[shape]) for shape in shapes)
    if total_size > area:
        return False

    def backtrack(i, current_fill):
        if i == len(shapes):
            return True

        for k, j in product(range(dim1), range(dim2)):
            if (k, j) in current_fill:
                continue
            for rotation in get_all_rotations(shape_defs[shapes[i]]):
                current_shape = {(x + k, y + j) for x, y in rotation}
                if current_fill.isdisjoint(current_shape) and in_bounding_box(
                    current_shape, dim1, dim2
                ):
                    if backtrack(i + 1, current_fill | current_shape):
                        return True
        return False

    return backtrack(0, set())


def main():
    puzzle = (row.strip() for row in fileinput.input())
    shape_defs = parse_shape_defs(puzzle)
    final_sum = 0
    for row in puzzle:
        area_def, shapes = parse_area_def(row)
        final_sum += int(can_fit(area_def, shapes, shape_defs))
    print(final_sum)


if __name__ == "__main__":
    main()
