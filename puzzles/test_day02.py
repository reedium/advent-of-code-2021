import pathlib
import pytest
import day02 as aoc

INPUTS_DIR = f"{pathlib.Path(__file__).parent.parent}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day02-example1.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day02_data():
    input_path = f"{INPUTS_DIR}/day02.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 150


def test_example2(example_data):
    assert aoc.part2(example_data) == 900


def test_part1(day02_data):
    assert aoc.part1(day02_data) == 1670340


def test_part2(day02_data):
    assert aoc.part2(day02_data) == 1954293920
