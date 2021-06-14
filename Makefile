.PHONY: check format tests

check:
	black --check --line-length 100 exercise.py
	black --check --line-length 100 tests.py
	flake8 --max-line-length 100 exercise.py
	flake8 --max-line-length 100 tests.py

format:
	black --line-length 100 exercise.py
	black --line-length 100 tests.py

tests:
	pytest tests.py --verbose