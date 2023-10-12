# Testing with FastAPI and Pytest,Hypothesis

This is a simple project to test `FastAPI` with `Pytest` and `Hypothesis`.

- `FastAPI` is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- `Pytest` is a testing framework for Python.
- `Hypothesis` is an advanced testing library for Python. It lets you write tests which are parametrized by a source of examples, and then generates simple and comprehensible examples that make your tests fail. This lets you find more bugs in your code with less work

## Type of tests

- `Unit tests`= test a single function, method, or class
- `Integration tests` = test how multiple pieces work together
- `End-to-end tests (e2e)` = test a complete flow of a application


## Customizing Test Behavior

You can customize the behavior of the tests by adding various options:

- `-v`: Verbose output, which provides detailed information about each test case.
- `--hypothesis-show-statistics`: Display Hypothesis statistics, showing the number of valid and invalid examples.
- `--hypothesis-deadline=<milliseconds>`: Set a specific deadline in milliseconds for test data generation.
- `--hypothesis-verbosity=verbose`: Enable verbose Hypothesis output for debugging and understanding data generation.
- `--hypothesis-phases=explicit`: Use explicit Hypothesis phases to control data generation.
- `--hypothesis-derandomize`: Enable derandomization for reproducible test data generation.


## How to run the tests


```bash
poetry run pytest -k "test_main.py" -v
poetry run pytest -k "test_main.py" -v --hypothesis-show-statistics
poetry run pytest -k "test_main.py" -v --hypothesis-show-statistics --hypothesis-deadline=1000
poetry run pytest -k "test_main.py" -v --hypothesis-show-statistics --hypothesis-deadline=1000 --hypothesis-verbosity=verbose
poetry run pytest -k "test_main.py" -v --hypothesis-show-statistics --hypothesis-deadline=1000 --hypothesis-verbosity=verbose --hypothesis-phases=explicit
poetry run pytest -k "test_main.py" -v --hypothesis-show-statistics --hypothesis-deadline=1000 --hypothesis-verbosity=verbose --hypothesis-phases=explicit --hypothesis-derandomize
```
