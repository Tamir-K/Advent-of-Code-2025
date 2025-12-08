#!/usr/bin/env python

# Imports
import fileinput
import math
from itertools import combinations
from collections import defaultdict
from functools import reduce
import heapq

# Constants
TUPLE = ","


def find_shortest_connections(coords, limit):
    return heapq.nsmallest(
        limit,
        (
            (math.dist(coord_1, coord_2), coord_1, coord_2)
            for coord_1, coord_2 in combinations(coords, 2)
        ),
    )


def find_n_largest_connected_components(coords, edges, n):
    # Create an adjacency list from edges
    graph = defaultdict(list)

    for _, u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Function to perform DFS and find all connected nodes
    def dfs(node, visited):
        visited.add(node)
        component_size = 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                component_size += dfs(neighbor, visited)
        return component_size

    visited = set()
    component_sizes = []

    for coord in coords:
        if coord not in visited:
            size = dfs(coord, visited)
            component_sizes.append(size)

    # Sort sizes and return the top 3
    component_sizes.sort(reverse=True)
    return component_sizes[:n]


def main():
    junction_boxes = [
        (int(x), int(y), int(z))
        for x, y, z in (row.strip().split(TUPLE) for row in fileinput.input())
    ]
    cables = find_shortest_connections(junction_boxes, 1000)
    largest_circuits = find_n_largest_connected_components(junction_boxes, cables, 3)
    print(reduce(lambda x, y: x * y, largest_circuits))


if __name__ == "__main__":
    main()
