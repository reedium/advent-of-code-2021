import pathlib
import pytest
import sys

ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(f"{ROOT_DIR}/puzzles")
import day05 as aoc

INPUTS_DIR = f"{ROOT_DIR}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day05-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day05_data():
    input_path = f"{INPUTS_DIR}/day05.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 5


def test_example2(example_data):
    assert aoc.part2(example_data) == 12


def test_part1(day05_data):
    assert aoc.part1(day05_data) == 6572


def test_part2(day05_data):
    assert aoc.part2(day05_data) == 21466
