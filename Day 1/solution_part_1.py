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
        dial = (dial + direction * int(line[DISTANCE:])) % 100
        if dial == 0:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
