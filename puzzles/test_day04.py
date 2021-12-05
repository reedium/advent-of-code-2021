import pathlib
import pytest
import day04 as aoc

INPUTS_DIR = f"{pathlib.Path(__file__).parent.parent}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day04-example.txt"
    return pathlib.Path(input_path).read_text().strip()


@pytest.fixture
def day04_data():
    input_path = f"{INPUTS_DIR}/day04.txt"
    return pathlib.Path(input_path).read_text().strip()


def test_example1(example_data):
    assert aoc.part1(example_data) == 4512


def test_example2(example_data):
    assert aoc.part2(example_data) == 1924


def test_part1(day04_data):
    assert aoc.part1(day04_data) == 25023


def test_part2(day04_data):
    assert aoc.part2(day04_data) == 2634
