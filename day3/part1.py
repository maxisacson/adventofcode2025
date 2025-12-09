#!/usr/bin/env python3

import sys


def parse_line(line):
    numbers = [int(c) for c in line.strip()]
    a = max(numbers[:-1])
    i = numbers.index(a, 0, -1)
    b = max(numbers[i+1:])
    n = 10*a + b
    return n


def main(input):
    total = sum(map(parse_line, input))
    print(total)


if __name__ == "__main__":
    main(sys.stdin)
