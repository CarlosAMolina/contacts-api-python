import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from contacts_api_python.main import app
from contacts_api_python.main import main

client = TestClient(app)


def test_get_contacts_if_no_search_term(_contacts_path_env):
    response = client.get("/contacts")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_contacts_if_search_term(_contacts_path_env):
    response = client.get("/contacts?search_term=john")
    assert response.status_code == 200
    assert len(response.json()) == 1


@pytest.fixture
def _contacts_path_env(monkeypatch):
    monkeypatch.setenv("contacts_path", "tests/fake/contacts.json")


def test_main_shows_contacts(_contacts_path_env):
    fake_path = Path("tests/fake")
    expected_result = (fake_path / "contacts-output.txt").read_text()
    output = StringIO()
    args = ["main.py", "john"]
    with (
        patch.object(sys, "argv", args),
        redirect_stdout(output),
    ):
        main()
    assert output.getvalue() == expected_result
