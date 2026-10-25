install:
	uv sync
	uvx pre-commit install

mypy:
	uv run mypy contacts_api_python

pre-commit:
	uvx pre-commit run --all-files

ruff-check:
	uv run ruff check .

ruff-fix:
	uv run ruff check . --fix

ruff-fix-unsafe:
	uv run ruff check . --fix --unsafe-fixes

ruff-format:
	uv run ruff format

run:
	uv run python -m contacts_api_python.main tests/fake/contacts.json jane

test:
	uv run pytest
