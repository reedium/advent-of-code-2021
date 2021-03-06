"""
Advent of Code 2021 - Day 02

Run with:
    python puzzles/day02.py inputs/day02.txt

This is overly complicated to mess around with classes
"""

import pathlib
import sys
from typing import List, Tuple


class Submarine:
    horizontal = 0
    depth = 0
    aim = 0

    def run(self, inputs: List[str]) -> int:
        for line in inputs:
            # forward 20 -> self.forward(20)
            step = line.split()
            getattr(self, step[0])(int(step[1]))

        return self.calculate()

    def calculate(self) -> int:
        return self.horizontal * self.depth


class Puzzle1(Submarine):
    def forward(self, distance: int) -> None:
        self.horizontal += distance

    def up(self, distance: int) -> None:
        self.depth -= distance

    def down(self, distance: int) -> None:
        self.depth += distance


class Puzzle2(Submarine):
    def forward(self, distance: int) -> None:
        self.horizontal += distance
        self.depth += self.aim * distance

    def up(self, distance: int) -> None:
        self.aim -= distance

    def down(self, distance: int) -> None:
        self.aim += distance


def parse(inputs: str) -> List[str]:
    """Parse the input string"""
    return inputs.split("\n")


def solve(path: str) -> Tuple[int, int]:
    """Solve the puzzle"""
    puzzle_input = parse(pathlib.Path(path).read_text().strip())

    part1 = Puzzle1()
    part2 = Puzzle2()

    return part1.run(puzzle_input), part2.run(puzzle_input)


def main() -> None:
    for path in sys.argv[1:]:
        print(f"Input File: {path}")

        part1_result, part2_result = solve(path)

        print(f"Part 1 Result: {part1_result}")
        print(f"Part 2 Result: {part2_result}")


if __name__ == "__main__":
    main()
