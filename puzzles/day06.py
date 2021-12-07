"""
Advent of Code 2021 - day 06

Run with:
    python puzzles/day06.py inputs/day06.txt
"""

import pathlib
import sys

from collections import Counter
from typing import List, Tuple


class Reproduce:
    times = None

    def __init__(self, times: List[int]) -> None:
        self.times = times

    def start(self, days: int = 80) -> None:
        counts = Counter(self.times)
        for _ in range(days):
            next_counts = Counter()  # Can't modify while iterating

            for count_key, count in counts.items():
                if count_key == 0:
                    next_counts[8] += count  # Add the new fish
                    next_counts[6] += count  # Move the parents back to 6 days
                else:
                    next_counts[count_key - 1] += count  # Move count to next day count

            counts = next_counts
        self.time_counts = counts

    def count_fish(self) -> int:
        return sum(self.time_counts.values())


def part1(inputs: List[int]) -> int:
    school = Reproduce(inputs)
    school.start(days=80)
    return school.count_fish()


def part2(inputs: List[int]) -> int:
    school = Reproduce(inputs)
    school.start(days=256)
    return school.count_fish()


def parse(inputs: str) -> List[int]:
    """Parse the input string"""
    return [int(value) for value in inputs.split(",")]


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
