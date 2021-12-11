import pathlib
import pytest
import sys

ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(f"{ROOT_DIR}/puzzles")
import day10 as aoc

INPUTS_DIR = f"{ROOT_DIR}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day10-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day10_data():
    input_path = f"{INPUTS_DIR}/day10.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 26397


def test_example2(example_data):
    assert aoc.part2(example_data) == 288957


def test_part1(day10_data):
    assert aoc.part1(day10_data) == 387363


def test_part2(day10_data):
    assert aoc.part2(day10_data) == 4330777059
