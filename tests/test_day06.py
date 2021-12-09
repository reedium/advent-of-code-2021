import pathlib
import pytest
import sys

ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(f"{ROOT_DIR}/puzzles")
import day06 as aoc

INPUTS_DIR = f"{ROOT_DIR}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day06-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day06_data():
    input_path = f"{INPUTS_DIR}/day06.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 5934


def test_example2(example_data):
    assert aoc.part2(example_data) == 26984457539


def test_part1(day06_data):
    assert aoc.part1(day06_data) == 386755


def test_part2(day06_data):
    assert aoc.part2(day06_data) == 1732731810807
