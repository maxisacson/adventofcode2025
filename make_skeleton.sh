#!/usr/bin/env bash

[[ -z $1 ]] && exit 1

day="$1"
mkdir -p "day$day"

[[ -f day$day/part1.py ]] && exit 1

cat <<EOF > "day$day/part1.py"
#!/usr/bin/env python

import sys


def main(input):
    pass


if __name__ == "__main__":
    main(sys.stdin)
EOF

chmod +x "day$day/part1.py"
