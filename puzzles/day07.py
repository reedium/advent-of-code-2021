"""
Advent of Code 2021 - Day 07

Run with:
    python puzzles/day07.py inputs/day07.txt
"""

import pathlib
import sys
from statistics import median
from typing import List, Tuple


class AlignCrabSubs:
    positions: List[int]

    def __init__(self, positions: List[int]) -> None:
        self.positions = positions

    def calc_fuel(self, pricey: bool = False) -> int:
        if not pricey:
            return self.calc_fuel_simple(median(self.positions))

        fuel = None
        for position in range(len(set(self.positions)) + 1):
            price = self.calc_fuel_pricey(position)
            if fuel is None or fuel > price:
                fuel = price

        return fuel

    def calc_fuel_simple(self, target: int) -> int:
        return int(sum(abs(num - target) for num in self.positions))

    def calc_fuel_pricey(self, target: int) -> int:
        fuel = 0
        for num in self.positions:
            num_range = abs(num - target) + 1
            fuel += sum(range(num_range))
        return int(fuel)


def part1(inputs: List[int]) -> int:
    subs = AlignCrabSubs(inputs)
    return subs.calc_fuel()


def part2(inputs: List[int]) -> int:
    subs = AlignCrabSubs(inputs)
    return subs.calc_fuel(pricey=True)


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
