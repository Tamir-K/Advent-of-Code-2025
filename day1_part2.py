#!/usr/bin/env python

# Imports
import fileinput

# Constants
DIRECTION = 0
DISTANCE = 1
LEFT = "L"


def main():
    dial = 50
    counter = 0

    for line in fileinput.input():
        direction = -1 if line[DIRECTION] == LEFT else 1
        distance = int(line[DISTANCE:])
        for _ in range(distance):
            dial += direction
            if dial > 99:
                dial -= 100
            elif dial < 0:
                dial += 100

            if dial == 0:
                counter += 1
    print(counter)


if __name__ == "__main__":
    main()
