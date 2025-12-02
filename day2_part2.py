#!/usr/bin/env python

# Imports
import fileinput

# Constants
RANGE_DELIMITER = ","
RANGE_INDICATOR = "-"
INCLUSIVE = 1


def main():
    id_ranges = next(fileinput.input()).split(RANGE_DELIMITER)
    bogus_id_sum = 0
    for id_range in id_ranges:
        lower_bound, upper_bound = id_range.split(RANGE_INDICATOR)
        bogus_ids = (
            id
            for id in range(int(lower_bound), int(upper_bound) + INCLUSIVE)
            if any(
                str(id)[: i + 1] * (len(str(id)) // (i + 1)) == str(id)
                for i in range(len(str(id)) // 2)
            )
        )
        bogus_id_sum += sum(bogus_ids)
    print(bogus_id_sum)


if __name__ == "__main__":
    main()
