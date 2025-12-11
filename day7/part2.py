#!/usr/bin/env python

import sys


def split_beam(i, rows, splits):
    for j,(prev,cur,s) in enumerate(zip(rows[i-1], rows[i], splits[i-1])):
        if prev == 'S':
            rows[i][j] = '|'
            splits[i][j] = 1
        elif prev == '|' and (cur == '.' or cur == '|'):
            rows[i][j] = '|'
            splits[i][j] += s
        elif prev == '|' and cur == '^':
            rows[i][j-1] = '|'
            rows[i][j+1] = '|'
            splits[i][j-1] += s
            splits[i][j+1] += s


def main(input):
    rows = [[c for c in row.strip()] for row in input]
    splits = [[0 for _ in row] for row in rows]

    for i in range(1, len(rows)):
        split_beam(i, rows, splits)

    print(sum(splits[-1]))


if __name__ == "__main__":
    main(sys.stdin)
