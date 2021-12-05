"""
Advent of Code 2021 - Day 05

Run with:
    python puzzles/day05.py inputs/day05.txt
"""

import pathlib
import sys
from typing import Dict, List, Tuple

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Location:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        self.x = int(self.x)
        self.y = int(self.y)


@dataclass
class VolcanicVent:
    start: Location
    end: Location

    def __post_init__(self):
        if self.start.x == self.end.x:
            self.direction = "vertical"
        elif self.start.y == self.end.y:
            self.direction = "horizontal"
        else:
            self.direction = "diagnal"


class Chart:
    chart: Dict = None
    vents: List = None

    def __init__(self, vents: List[VolcanicVent], diagnals: bool = True) -> None:
        self.vents = vents
        self._generate_chart(diagnals=diagnals)

    def _generate_chart(self, diagnals: bool = True) -> None:
        """
        .......1..
        ..1....1..
        ..1....1..
        .......1..
        .112111211
        ..........
        ..........
        ..........
        ..........
        222111....      0,9 -> 5,9      0,9 -> 2,9
        """
        self.chart = defaultdict(int)
        for vent in self.vents:
            if vent.direction != "diagnal":
                self._chart_line_horiz_vert(vent.start, vent.end)
            elif diagnals:
                self._chart_line_diagnal(vent.start, vent.end)

    def _chart_line_diagnal(self, start: Location, end: Location) -> None:
        if end.x > start.x:  # direction: left
            x_range = range(start.x, end.x + 1)
        else:  # direction: right
            x_range = range(start.x, end.x - 1, -1)  # reverse range
        if end.y > start.y:  # direction: down
            y_range = range(start.y, end.y + 1)
        else:  # direction: up
            y_range = range(start.y, end.y - 1, -1)  # reverse range

        for x, y in zip(x_range, y_range):
            self.chart[x, y] += 1

    def _chart_line_horiz_vert(self, start: Location, end: Location) -> None:
        min_x = min(start.x, end.x)
        max_x = max(start.x, end.x)
        min_y = min(start.y, end.y)
        max_y = max(start.y, end.y)

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                self.chart[x, y] += 1

    def calculate_overlaps(self, max_depth: int = 1) -> int:
        return sum(depth_count > max_depth for depth_count in self.chart.values())


def part1(inputs: List[int]) -> int:
    c = Chart(inputs, diagnals=False)
    return c.calculate_overlaps()


def part2(inputs: List[int]) -> int:
    c = Chart(inputs)
    return c.calculate_overlaps()


def parse(inputs: str) -> List[int]:
    """Parse the input string"""
    results = []
    for line in inputs.split("\n"):
        start_end = line.split(" -> ")
        results.append(
            VolcanicVent(
                start=Location(*start_end[0].split(",")),
                end=Location(*start_end[1].split(",")),
            )
        )
    return results


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
