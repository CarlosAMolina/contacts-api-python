import pytest


@pytest.fixture
def contacts_path_env_fixture(monkeypatch):
    monkeypatch.setenv("contacts_path", "tests/fake/contacts.json")
