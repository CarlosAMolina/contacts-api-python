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

# Example: make run-api CONTACTS_PATH=~/Downloads/contacts.json
run-api:
	sleep 1 && open http://127.0.0.1:8000/docs & # sleep and & to wait until the next command finish
	contacts_path="$(CONTACTS_PATH)" \
		uv run fastapi dev

run-api-dev:
	contacts_path=tests/fake/contacts.json \
		uv run fastapi dev

test:
	uv run pytest

# Example: make test-filter TEST_FILTER=test_get_contact_if_contact_id_does_not_exist
test-filter:
	uv run pytest -vvk "$(TEST_FILTER)"
