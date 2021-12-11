"""
Advent of Code 2021 - Day 10

Run with:
    python puzzles/day10.py inputs/day10.txt
"""

import pathlib
import sys
from typing import Dict, List, Tuple

from statistics import median


class Subsystem:
    nav_data = None
    open_chars = ["(", "[", "{", "<"]
    close_chars = [")", "]", "}", ">"]

    def __init__(self, inputs: List[str]) -> None:
        self.nav_data = inputs
        self.validate()

    def validate(self) -> None:
        chunks = {"corrupted": [], "incomplete": [], "complete": []}
        corrupted_chars = []
        incomplete_chunks = []

        for line in self.nav_data:
            corrupted = False

            opens = []
            for char in line:
                if char in self.open_chars:
                    opens.append(char)
                    continue

                open_char = self.open_chars[self.close_chars.index(char)]
                if opens[-1] != open_char:
                    corrupted = True
                    corrupted_chars.append(char)
                    break

                del opens[-1]  # Clear the open bracket

            if corrupted:
                chunks["corrupted"].append(line)
            elif len(opens) != 0:
                chunks["incomplete"].append(line)
                incomplete_chunks.append(opens)
            else:
                chunks["complete"].append(line)

        self.chunks = chunks
        self.corrupted_chars = corrupted_chars
        self.incomplete_chunks = incomplete_chunks

    def score_corrupted(self) -> int:
        scores = {")": 3, "]": 57, "}": 1197, ">": 25137,}
        return sum([scores[char] for char in self.corrupted_chars])

    def score_incomplete(self) -> int:
        scores = {")": 1, "]": 2, "}": 3, ">": 4,}
        total_scores = []
        for chunk in self.incomplete_chunks:
            total_score = 0
            for char in reversed(chunk):
                close_char = self.close_chars[self.open_chars.index(char)]
                total_score = total_score * 5 + scores[close_char]
            total_scores.append(total_score)

        return median(total_scores)


def part1(inputs: List[int]) -> int:
    s = Subsystem(inputs)
    return s.score_corrupted()


def part2(inputs: List[int]) -> int:
    s = Subsystem(inputs)
    return s.score_incomplete()


def parse(inputs: str) -> List[int]:
    """Parse the input string"""
    return inputs.split()


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
