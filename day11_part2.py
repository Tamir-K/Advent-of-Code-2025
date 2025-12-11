#!/usr/bin/env python

# Imports
import fileinput
from functools import cache
from collections import defaultdict
from itertools import pairwise
from functools import reduce


# Constants
DELIMITER = ":"
PATH = ["svr", "fft", "dac", "out"]


def count_paths(graph, start, end):
    @cache
    def inner(start_node, end_node):
        return (
            1
            if start_node == end_node
            else sum(inner(connection, end_node) for connection in graph[start_node])
        )

    return inner(start, end)


def main():
    puzzle = (row.strip().split(DELIMITER) for row in fileinput.input())
    device_dag_neighbors = defaultdict(
        list, {device: connections.split() for device, connections in puzzle}
    )
    paths = reduce(
        lambda left, right: left * right,
        (count_paths(device_dag_neighbors, *pair) for pair in pairwise(PATH)),
    )
    print(paths)


if __name__ == "__main__":
    main()
