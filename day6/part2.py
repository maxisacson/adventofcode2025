#!/usr/bin/env python

import sys


def main(input):
    chars = [[c for c in row.strip('\n')] for row in input]
    ops = chars[-1]
    ops = list(reversed([op for op in ops if op != ' ']))
    chars.pop(-1)
    chars = [list(col) for col in zip(*chars)]

    nums = [''.join(c).strip() for c in reversed(chars)] + ['']

    problems = []
    p = []
    for n in nums:
        if n == '':
            p.append(ops.pop(0))
            problems.append(p)
            p = []
            continue
        p.append(n)

    results = [eval(p[-1].join(p[:-1])) for p in problems]
    print(sum(results))


if __name__ == "__main__":
    main(sys.stdin)
