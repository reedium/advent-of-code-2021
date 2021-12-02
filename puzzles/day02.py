"""
Advent of Code 2021 - Day 02

Run with:
    python puzzles/day02.py inputs/day02.txt
"""

import pathlib
import sys
from typing import List, Tuple

def part1(inputs: List[int], horizontal: int=0, depth: int=0) -> int:
    for line in inputs:
        step = line.split()
        if step[0] == "forward":
            horizontal += int(step[1])
        elif step[0] == "up":
            depth -= int(step[1])
        elif step[0] == "down":
            depth += int(step[1])
    return horizontal * depth


def part2(inputs: List[int], horizontal: int=0, depth: int=0, aim: int=0) -> int:
    for line in inputs:
        step = line.split()
        if step[0] == "forward":
            horizontal += int(step[1])
            depth += aim * int(step[1])
        elif step[0] == "up":
            aim -= int(step[1])
        elif step[0] == "down":
            aim += int(step[1])
    return horizontal * depth


def parse(inputs: str) -> List[List[str]]:
    """Parse the input string"""
    return inputs.split("\n")


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

if __name__ == "__main__":
    main()
