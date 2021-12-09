import pathlib
import pytest
import sys

ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(f"{ROOT_DIR}/puzzles")
import day01 as aoc

INPUTS_DIR = f"{ROOT_DIR}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day01-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day01_data():
    input_path = f"{INPUTS_DIR}/day01.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 7


def test_example2(example_data):
    assert aoc.part2(example_data) == 5


def test_part1(day01_data):
    assert aoc.part1(day01_data) == 1266


def test_part2(day01_data):
    assert aoc.part2(day01_data) == 1217
