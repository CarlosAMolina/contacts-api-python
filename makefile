install:
	uv sync
	uvx pre-commit install

mypy:
	uv run mypy src/contacts_api_python

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
	contacts_path=src/tests/fake/contacts.json \
		uv run python -m src.contacts_api_python.main jane

run-fastapi-dev:
	contacts_path=src/tests/fake/contacts.json \
		uv run fastapi dev

test:
	uv run pytest
