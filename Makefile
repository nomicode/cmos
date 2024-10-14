.PHONY: install install-package update test

install:
	poetry install

install-package:
	poetry install --no-dev

update:
	poetry update

test:
	poetry run pytest
