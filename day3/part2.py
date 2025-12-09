#!/usr/bin/env python3

import sys


def parse_line(line):
    numbers = [int(c) for c in line.strip()]

    k = 12
    n = 0
    while k > 0:
        k -= 1
        last = len(numbers) - k
        d = max(numbers[:last])
        i = numbers.index(d, 0, last)
        numbers = numbers[i+1:]
        n += (10**k)*d
    return n


def main(input):
    total = sum(map(parse_line, input))
    print(total)


if __name__ == "__main__":
    main(sys.stdin)
