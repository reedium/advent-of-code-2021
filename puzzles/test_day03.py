"""
Remove the 'Not implemented' marks when ready to run the test
"""
import pathlib
import pytest
import day03 as aoc

INPUTS_DIR = f"{pathlib.Path(__file__).parent.parent}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day03-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day03_data():
    input_path = f"{INPUTS_DIR}/day03.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 198


def test_example2(example_data):
    assert aoc.part2(example_data) == 230


def test_part1(day03_data):
    assert aoc.part1(day03_data) == 3885894


def test_part2(day03_data):
    assert aoc.part2(day03_data) == 4375225
