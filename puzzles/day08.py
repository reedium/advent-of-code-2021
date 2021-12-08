"""
Advent of Code 2021 - Day 08

Run with:
    python puzzles/day08.py inputs/day08.txt
"""

import pathlib
import sys
from collections import defaultdict
from typing import List, Tuple


class Display:
    """
     0 (6)   1 (2*)  2 (5)   3 (5)  4 (4*)
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

     5 (5)   6 (6)   7 (3*)  8 (7*)  9 (6)
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    """

    def __init__(self, entries: List[str]):
        self.entries = self._parse(entries)

    def decode(self):
        results = []

        for entry in self.entries:
            cipher = self._generate_cipher(entry["signals"])
            decrypt = self._decrypt(cipher, entry["outputs"])
            results.append(decrypt)

        return sum(results)

    def unique_count(self):
        unique = 0
        for entry in self.entries:
            unique += self._get_unique(entry)
        return unique

    @staticmethod
    def _decrypt(cipher, enc_string):
        output = ""
        for code in enc_string:
            output += str(cipher["".join(sorted(code))])
        return int(output)

    @staticmethod
    def _generate_cipher(entry):
        codes = {}  # Length: Actual Number
        filtered = defaultdict(list)
        for signal in entry:
            filtered[len(signal)].append(set(signal))

        codes[1] = filtered[2][0]
        codes[4] = filtered[4][0]
        codes[7] = filtered[3][0]
        codes[8] = filtered[7][0]

        for code in filtered[5]:
            if len(code.union(codes[1])) == 5:
                codes[3] = code
            elif len(code.union(codes[4])) == 7:
                codes[2] = code
            else:
                codes[5] = code

        for code in filtered[6]:
            if len(code.union(codes[7])) == 7:
                codes[6] = code
            elif len(code.union(codes[5])) == 6:
                codes[9] = code
            else:
                codes[0] = code

        # Let's reformat the results so we can reference by string
        results = {"".join(sorted(code)): value for value, code in codes.items()}

        return results

    @staticmethod
    def _get_unique(entries):
        unique = 0
        for entry in entries["outputs"]:
            length = len(entry)
            unique += length in [2, 4, 3, 7]  # 1,4,7,8
        return unique

    @staticmethod
    def _parse(lines):
        entries = []
        for line in lines:
            split = line.split()
            entries.append({
                "signals": list(split[0:10]),
                "outputs": list(split[11:]),
            })

        return entries





def part1(inputs: List[int]) -> int:
    d = Display(inputs)
    return d.unique_count()


def part2(inputs: List[int]) -> int:
    d = Display(inputs)
    return d.decode()


def parse(inputs: str) -> List[int]:
    """Parse the input string"""
    return [line for line in inputs.split("\n")]


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
