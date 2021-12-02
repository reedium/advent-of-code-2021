"""
TEMPLATE FOR ADVENT OF CODE

REPLACE EXAMPLES:
    * dayXX -> day01 
    * Day XX -> Day 01

Advent of Code 2021 - Day XX

Run with:
    python puzzles/dayXX.py inputs/dayXX.txt
"""

import pathlib
import sys
from typing import List, Tuple

def part1(inputs: List[int]) -> int:
    return False


def part2(inputs: List[int]) -> int:
    return False


def parse(inputs: str) -> List[int]:
    """Parse the input string"""
    return [int(line) for line in inputs.split()]


def solve(path: str) -> Tuple[int, int]:
    """Solve the puzzle"""
    puzzle_input = parse(pathlib.Path(path).read_text().strip())
    part1_result = part1(puzzle_input)
    part2_result = part2(puzzle_input)

    return part1_result, part2_result


def main() -> None:
    for path in sys.argv[1:]:
        print(f"Input File: {path}")

        part1_result, part2_result = solve(path)

        print(f"Part 1 Result: {part1_result}")
        print(f"Part 2 Result: {part2_result}")
