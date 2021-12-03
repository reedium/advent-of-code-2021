# Overview

My solutions for [Advent of Code](https://adventofcode.com)

Hopefully I keep up with it


# Installation
```
git clone https://gitea.ryanreed.net:3000/ryanreed/aoc2021.git
cd 2021-advent-of-code
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.text
```


# Testing/Verifying Solutions

Each day will include a pytest script that uses examples from the day.
This allows for verifying the code works by running `pytest`. For example:

```
|--% pytest -v puzzles/test_day01.py
=========================================== test session starts ===========================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- .venv/bin/python3
cachedir: .pytest_cache
rootdir: 2021-advent-of-code
collected 4 items

puzzles/test_day01.py::test_example1 PASSED                                                         [ 25%]
puzzles/test_day01.py::test_example2 PASSED                                                         [ 50%]
puzzles/test_day01.py::test_part1 PASSED                                                            [ 75%]
puzzles/test_day01.py::test_part2 PASSED                                                            [100%]

============================================ 4 passed in 0.06s ============================================
```
