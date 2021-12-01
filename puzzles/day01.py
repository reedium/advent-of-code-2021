"""
Advent of Code 2021 - Day 01

Run with:
    python puzzles/day01.py inputs/day01.txt
"""
import pathlib
import sys
from typing import Dict, List, Tuple

from numpy import sum as np_sum
from numpy.lib.stride_tricks import sliding_window_view


def compare(inputs: List[int]) -> Dict[str, int]:
    result = {"increased": 0, "decreased": 0, "no change": 0, "n/a": 0}
    prev = None
    for cur in inputs:
        status = "no change"
        if prev is None:
            status = "n/a"
        elif cur > prev:
            status = "increased"
        elif cur < prev:
            status = "decreased"
        result[status] += 1
        prev = cur
    return result


def part1(inputs: List[int]) -> int:
    """
    Count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

    199 (N/A - no previous measurement)
    200 (increased)
    208 (increased)
    210 (increased)
    200 (decreased)
    207 (increased)
    240 (increased)
    269 (increased)
    260 (decreased)
    263 (increased)

    In this example, there are 7 measurements that are larger than the previous measurement.
    """
    return compare(inputs).get("increased", 0)


def part2(inputs: List[int]) -> int:
    """
    Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

    Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

    In the above example, the sum of each three-measurement window is as follows:

    A: 607 (N/A - no previous sum)
    B: 618 (increased)
    C: 618 (no change)
    D: 617 (decreased)
    E: 647 (increased)
    F: 716 (increased)
    G: 769 (increased)
    H: 792 (increased)

    In this example, there are 5 sums that are larger than the previous sum
    """
    inputs = np_sum(sliding_window_view(inputs, window_shape=3), axis=1)
    return compare(inputs).get("increased", 0)


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


if __name__ == "__main__":
    main()
