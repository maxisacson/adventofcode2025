#!/usr/bin/env python

import sys


def split_beam(i, rows):
    n = 0
    for j,(prev,cur) in enumerate(zip(rows[i-1], rows[i])):
        if prev == 'S':
            rows[i][j] = '|'
        elif prev == '|' and cur == '.':
            rows[i][j] = '|'
        elif prev == '|' and cur == '^':
            rows[i][j-1] = '|'
            rows[i][j+1] = '|'
            n += 1

    return n


def main(input):
    rows = [[c for c in row.strip()] for row in input]

    n = 0
    for i in range(1, len(rows)):
        n += split_beam(i, rows)

    print(n)


if __name__ == "__main__":
    main(sys.stdin)
