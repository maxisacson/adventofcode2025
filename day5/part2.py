#!/usr/bin/env python

import sys


def merge_ranges(ranges):
    merged = sorted(ranges, key=lambda x: x[0], reverse=True)

    for i in reversed(range(1, len(merged))):
        a1, b1 = merged[i]
        a2, b2 = merged[i-1]
        if a2 > b1:
            continue
        merged[i-1] = (a1, max(b1, b2))
        merged.pop(i)

    return list(reversed(merged))


def count_fresh(ranges):
    count = 0
    for a,b in ranges:
        count += b - a + 1
    return count


def main(input):
    ranges = []

    for line in input:
        if len(line.strip()) == 0:
            break
        ranges.append(tuple(int(x) for x in line.strip().split('-')))

    ranges = merge_ranges(ranges)
    count = count_fresh(ranges)
    print(count)


if __name__ == "__main__":
    main(sys.stdin)
