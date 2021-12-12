"""
Advent of Code 2021 - Day 11

Run with:
    python puzzles/day11.py inputs/day11.txt
"""

import pathlib
import sys
from typing import List, Tuple

from dataclasses import dataclass


@dataclass
class Octopus:
    energy_level: int = 0
    flash_count: int = 0
    location: Tuple[int, int] = (0, 0)
    last_flash: int = 0


class School:
    octopi = None
    step = 1

    def __init__(self, data: List[str]) -> None:
        self.parse(data)
        self.synchronized_steps = []

    def flash(self, octopus: Octopus) -> None:
        octopus.energy_level = 0
        octopus.flash_count += 1
        octopus.last_flash = self.step
        self.update_neighbors(octopus.location)

    def update(self, octopus: Octopus) -> None:
        if octopus.last_flash == self.step:
            return None

        octopus.energy_level += 1
        if octopus.energy_level == 10:
            self.flash(octopus)

    def update_neighbors(self, location: Tuple[int, int]) -> None:
        min_row = 0 if location[0] == 0 else location[0] - 1
        min_col = 0 if location[1] == 0 else location[1] - 1
        max_row = (
            location[0] if location[0] == self.size["rows"] - 1 else location[0] + 1
        )
        max_col = (
            location[1] if location[1] == self.size["cols"] - 1 else location[1] + 1
        )

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                if row == location[0] and col == location[1]:
                    continue
                if self.octopi[row][col].last_flash == self.step:
                    continue

                self.update(self.octopi[row][col])

    def simulate(self, steps: int = 100) -> None:
        for step in range(1, steps + 1):
            self.step = step
            for row in self.octopi:
                for octopus in row:
                    self.update(octopus)

    def is_synchronized(self) -> bool:
        """This is inefficient and needs to be reworked"""
        for row in self.octopi:
            for octopi in row:
                if octopi.energy_level > 0:
                    return False

        return True

    @property
    def first_synchronized(self) -> int:
        step = 0
        while True:
            step += 1
            self.step = step
            for row in self.octopi:
                for octopus in row:
                    self.update(octopus)

            if self.is_synchronized():
                break

        return step

    @property
    def total_flashes(self) -> int:
        total = 0
        for row in self.octopi:
            for octopus in row:
                total += octopus.flash_count

        return total

    def parse(self, data: List[str]) -> None:
        self.octopi = []
        for row_index, row in enumerate(data):
            self.octopi.append(
                [
                    Octopus(
                        energy_level=int(value),
                        location=(int(row_index), int(column_index)),  # row, col
                    )
                    for column_index, value in enumerate(row)
                ]
            )
        self.size = {"rows": len(self.octopi), "cols": len(self.octopi[0])}


def part1(inputs: List[int]) -> int:
    s = School(inputs)
    s.simulate()
    return s.total_flashes


def part2(inputs: List[int]) -> int:
    s = School(inputs)
    return s.first_synchronized


def parse(inputs: str) -> List[str]:
    """Parse the input string"""
    return [line for line in inputs.split()]


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
