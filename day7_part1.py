#!/usr/bin/env python

# Imports
import fileinput

# Constants
START_POINT = "S"
OBSTACLE = "^"


def main():
    puzzle = fileinput.input()
    beams = {pos for pos, char in enumerate(next(puzzle)) if char == START_POINT}
    splits = 0
    for row in puzzle:
        obstacles = {pos for pos, char in enumerate(row) if char == OBSTACLE}
        for obstacle in obstacles:
            if obstacle in beams:
                beams.remove(obstacle)
                beams.update({obstacle - 1, obstacle + 1})
                splits += 1
    print(splits)


if __name__ == "__main__":
    main()
