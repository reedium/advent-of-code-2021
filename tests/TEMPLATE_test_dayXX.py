"""
Replace `dayXX` with the day number (e.g. `day01`)

Remove the 'Not implemented' marks when ready to run the test
"""
import pathlib
import pytest
import sys

ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(f"{ROOT_DIR}/puzzles")
import dayXX as aoc

INPUTS_DIR = f"{ROOT_DIR}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/dayXX-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def dayXX_data():
    input_path = f"{INPUTS_DIR}/dayXX.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.mark.skip(reason="Not implemented")
def test_example1(example_data):
    assert aoc.part1(example_data) == ...


@pytest.mark.skip(reason="Not implemented")
def test_example2(example_data):
    assert aoc.part2(example_data) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1(dayXX_data):
    assert aoc.part1(dayXX_data) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2(dayXX_data):
    assert aoc.part2(dayXX_data) == ...
