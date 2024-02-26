.PHONY: test run

run:
	python main.py

test:
	python -m unittest discover test/