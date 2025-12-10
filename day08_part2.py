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


def kruskals_algorithm(coords):
    edges = sorted(
        (math.dist(coord_1, coord_2), coord_1, coord_2)
        for coord_1, coord_2 in combinations(coords, 2)
    )

    # Union-Find data structure
    parent = {coord: coord for coord in coords}
    rank = {coord: 0 for coord in coords}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        rootU = find(u)
        rootV = find(v)
        if rootU != rootV:
            if rank[rootU] > rank[rootV]:
                parent[rootV] = rootU
            elif rank[rootU] < rank[rootV]:
                parent[rootU] = rootV
            else:
                parent[rootV] = rootU
                rank[rootU] += 1

    # Selecting the edges
    selected_edges = []
    for edge in edges:
        distance, u, v = edge
        if find(u) != find(v):
            union(u, v)
            selected_edges.append(edge)

    return selected_edges


def main():
    junction_boxes = [
        (int(x), int(y), int(z))
        for x, y, z in (row.strip().split(TUPLE) for row in fileinput.input())
    ]
    connecting_cable = kruskals_algorithm(junction_boxes)[-1]
    _, u, v = connecting_cable
    x1, _, _ = u
    x2, _, _ = v
    print(x1 * x2)


if __name__ == "__main__":
    main()
