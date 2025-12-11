#!/usr/bin/env python

import sys


def main(input):
    rows = [[col for col in row.split()] for row in input]
    problems = [list(col) for col in zip(*rows)]
    results = [eval(p[-1].join(p[:-1])) for p in problems]
    print(sum(results))


if __name__ == "__main__":
    main(sys.stdin)
