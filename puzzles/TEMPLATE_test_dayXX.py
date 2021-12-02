"""
Replace `dayXX` with the day number (e.g. `day01`)

Remove the 'Not implemented' marks when ready to run the test
"""
import pathlib
import pytest
import dayXX as aoc

INPUTS_DIR = f"{pathlib.Path(__file__).parent.parent}/inputs"

@pytest.fixture
def example_data1():
    input_path = f"{INPUTS_DIR}/dayXX-example1.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())

@pytest.fixture
def example_data2():
    input_path = f"{INPUTS_DIR}/dayXX-example2.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def dayXX_data():
    input_path = f"{INPUTS_DIR}/dayXX.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.mark.skip(reason="Not implemented")
def test_example1(example_data1):
    assert aoc.part1(example_data1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_example2(example_data2):
    assert aoc.part2(example_data2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1(day02_data):
    assert aoc.part1(day02_data) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2(day02_data):
    assert aoc.part2(day02_data) == ...
