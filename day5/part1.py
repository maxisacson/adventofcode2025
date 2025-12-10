#!/usr/bin/env python

import sys


def main(input):
    ranges = []

    for line in input:
        if len(line.strip()) == 0:
            break
        ranges.append(tuple(int(x) for x in line.strip().split('-')))

    ids = [int(line.strip()) for line in input]

    count = sum(any(a <= id <= b for (a, b) in ranges) for id in ids)
    print(count)


if __name__ == "__main__":
    main(sys.stdin)
