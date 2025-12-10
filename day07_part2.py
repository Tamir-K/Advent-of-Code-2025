#!/usr/bin/env python

# Imports
import fileinput
from collections import defaultdict

# Constants
START_POINT = "S"
OBSTACLE = "^"


def main():
    puzzle = fileinput.input()
    beams = {pos: 1 for pos, char in enumerate(next(puzzle)) if char == START_POINT}
    beams = defaultdict(int, beams)
    for row in puzzle:
        obstacles = {pos for pos, char in enumerate(row) if char == OBSTACLE}
        for obstacle in obstacles:
            if obstacle in beams:
                beams[obstacle + 1] += beams[obstacle]
                beams[obstacle - 1] += beams[obstacle]
                del beams[obstacle]
    print(sum(beams.values()))


if __name__ == "__main__":
    main()
