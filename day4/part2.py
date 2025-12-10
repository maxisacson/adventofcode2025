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


def remove_accessible(grid):
    grid2 = [[col for col in row] for row in grid]

    n = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != '@':
                continue
            k = count_neighbours(grid, r, c)
            if k < 4:
                n += 1
                grid2[r][c] = '.'

    return grid2, n


def main(input):
    grid = [[c for c in line.strip()] for line in input]

    n = 1
    total = 0
    while n > 0:
        grid, n = remove_accessible(grid)
        total += n

    print(total)


if __name__ == "__main__":
    main(sys.stdin)
