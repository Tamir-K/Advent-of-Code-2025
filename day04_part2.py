#!/usr/bin/env python

# Imports
import fileinput
import numpy as np
from scipy.signal import convolve2d

# Constants
PAPER_ROLL = "@"
NEIGHBOURS = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
THRESHOLD = 4


def sum_neighbours(matrix: np.ndarray) -> np.ndarray:
    """Sum neighboring cells for each cell in matrix"""
    kernel = np.array(NEIGHBOURS)
    neighbor_counts = convolve2d(
        matrix, kernel, mode="same", boundary="fill", fillvalue=0
    )
    return neighbor_counts


def main():
    paper_roll_matrix = np.array(
        [
            [1 if char == PAPER_ROLL else 0 for char in line.strip()]
            for line in fileinput.input()
        ]
    )
    paper_roll_count = 0
    while True:
        neighbor_counts = sum_neighbours(paper_roll_matrix)
        accessible_paper_rolls = (neighbor_counts < THRESHOLD) & paper_roll_matrix
        accessible_paper_roll_count = np.sum(accessible_paper_rolls)
        if accessible_paper_roll_count == 0:
            break
        paper_roll_count += accessible_paper_roll_count
        paper_roll_matrix -= accessible_paper_rolls

    print(paper_roll_count)


if __name__ == "__main__":
    main()
