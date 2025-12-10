#!/usr/bin/env python

import sys


def count_neighbours(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    n = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and c == col:
                continue
            if 0 <= r < rows and 0 <= c < cols:
                n += (grid[r][c] == '@')
    return n


def count_accessible(grid):
    n = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != '@':
                continue
            k = count_neighbours(grid, r, c)
            n += (k < 4)
    return n


def main(input):
    grid = [[c for c in line.strip()] for line in input]
    print(count_accessible(grid))


if __name__ == "__main__":
    main(sys.stdin)
