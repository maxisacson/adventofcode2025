#!/usr/bin/env bash

source .env

YEAR=2025
day="$1"

if [[ -z $day ]]; then
    day="$(date "+%-d")"
fi

if ! [[ -f day${day}/input.txt ]]; then
    curl -s -b "session=$AOC_SESSION" https://adventofcode.com/${YEAR}/day/${day}/input -o "day${day}/input.txt"
fi
