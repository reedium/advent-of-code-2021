"""
Advent of Code 2021 - Day 03

Run with:
    python puzzles/day03.py inputs/day03.txt
"""

import pathlib
import sys
from typing import Dict, List, Tuple

from collections import defaultdict


class Diagnostics:
    report_data = None

    def __init__(self, report: List[int]) -> None:
        self.report_data = report

    def calc_power_usage(self) -> int:
        most_common = self.commonality(self.report_data)
        gamma = epsilon = ""
        for common in most_common:
            if common == 1:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"

        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
        return gamma * epsilon

    def calc_life_support_rating(self) -> int:
        oxygen_generator_rating = self.calc_oxygen_generator_rating()
        co2_scrubber_rating = self.calc_co2_scrubber_rating()
        return oxygen_generator_rating * co2_scrubber_rating


    def calc_oxygen_generator_rating(self) -> int:
        """
        Bit Criteria:
            Most common value in current bit position
                If 0 and 1 are equally common, keep values with a 1
            Keep only values with this bit in this position
        """
        report = self.report_data.copy()
        for column in range(len(report[0])):
            most_common = self.commonality(report)
            for binary in list(report):
                if (
                    int(binary[column]) != most_common[column]
                    and most_common[column] != 2
                ) or (most_common[column] == 2 and binary[column] != "1"):
                    report.remove(binary)

                if len(report) == 1:
                    return int(report[0], 2)

        return 0 # Failsafe

    def calc_co2_scrubber_rating(self) -> int:
        """
        Bit Criteria:
          Least common value in current position
              If 0 and 1 are equally common, keep values with a 0
          Keep only values with this bit in this position
        """
        report = self.report_data.copy()
        for column in range(len(report[0])):
            most_common = self.commonality(report)
            for binary in list(report):
                if (int(binary[column]) == most_common[column]) or (
                    most_common[column] == 2 and binary[column] != "0"
                ):
                    report.remove(binary)

                if len(report) == 1:
                    return int(report[0], 2)

        return 0 # Failsafe


    @staticmethod
    def commonality(report: List[str]) -> List[int]:
        """
        Return the most common value in each column of binary numbers

        Args:
            report: List of binary numbers

        Returns:
            List containing the most common value in the column
            Possible Values:
                0
                1
                2 - This indicates equally common
        """
        num_1 = defaultdict(int)
        for binary in report:
            for column, bit in enumerate(binary):
                num_1[column] += int(bit)

        common = []
        half_total = len(report) / 2
        for count in num_1.values():
            if count == half_total:
                common.append(2)  # Indicating equally common
            elif count > half_total:
                common.append(1)
            else:
                common.append(0)

        return common


def part1(inputs: List[int]) -> int:
    diag = Diagnostics(inputs)
    return diag.calc_power_usage()


def part2(inputs: List[int]) -> int:
    diag = Diagnostics(inputs)
    return diag.calc_life_support_rating()


def parse(inputs: str) -> List[int]:
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
