"""
Advent of Code 2021 - Day 04

Run with:
    python puzzles/day04.py inputs/day04.txt
"""

import pathlib
import sys
from typing import Dict, List, Tuple

import numpy as np


class Bingo:
    boards = None
    draws = None

    def __init__(self, inputs: str) -> None:
        inputs = inputs.split("\n\n")

        # Convert all values to int
        self.draws = list(map(int, inputs.pop(0).split(",")))
        self.boards = np.array(
            [
                [list(map(int, value.split())) for value in line.split("\n")]
                for line in inputs
            ],
            dtype=object,
        )

    def solve(self, squid_rules: bool = False) -> int:
        game = self.boards.copy()
        winning_scores = []
        for draw in self._draw():
            game[game == draw] = np.nan

            for index, board in enumerate(game):
                if self._is_solved(board):
                    winning_scores.append(self._calculate_score(board, draw))

                    if not squid_rules:
                        return winning_scores[0]

                    try:
                        game = np.delete(game, index, axis=0)
                    except IndexError:  # I don't understand why this is needed
                                        # Need to rework the whole class
                                        # Wrong way to go about this
                        pass

            if len(winning_scores) == np.size(self.boards, axis=0):
                break

        index = -1 if squid_rules else 0
        return winning_scores[index]

    def _draw(self) -> int:
        for draw in self.draws:
            yield draw

    @staticmethod
    def _calculate_score(solved_board, last_draw: int) -> int:
        board_score = np.nansum(solved_board)
        return board_score * last_draw

    @staticmethod
    def _is_solved(board) -> bool:
        # Solved if any row or column is 0
        cols = np.nansum(board, axis=0)
        rows = np.nansum(board, axis=1)
        return (np.count_nonzero(cols) != cols.size or np.count_nonzero(rows) != rows.size)


def part1(inputs: str) -> int:
    game = Bingo(inputs)
    return game.solve()


def part2(inputs: str) -> int:
    game = Bingo(inputs)
    return game.solve(squid_rules=True)


def solve(path: str) -> Tuple[int, int]:
    """Solve the puzzle"""
    inputs = pathlib.Path(path).read_text().strip()
    part1_result = part1(inputs)
    part2_result = part2(inputs)

    return part1_result, part2_result


def main() -> None:
    for path in sys.argv[1:]:
        print(f"Input File: {path}")

        part1_result, part2_result = solve(path)

        print(f"Part 1 Result: {part1_result}")
        print(f"Part 2 Result: {part2_result}")


if __name__ == "__main__":
    main()
