import pathlib
import pytest
import day07 as aoc

INPUTS_DIR = f"{pathlib.Path(__file__).parent.parent}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day07-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day07_data():
    input_path = f"{INPUTS_DIR}/day07.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 37


def test_example2(example_data):
    assert aoc.part2(example_data) == 168


def test_part1(day07_data):
    assert aoc.part1(day07_data) == 343441


def test_part2(day07_data):
    assert aoc.part2(day07_data) == 98925151
