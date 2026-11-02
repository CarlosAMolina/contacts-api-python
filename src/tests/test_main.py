import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest

from contacts_api_python.main import main


@pytest.fixture
def _contacts_path_env(monkeypatch):
    monkeypatch.setenv("contacts_path", "src/tests/fake/contacts.json")


def test_main_shows_contacts(_contacts_path_env):
    fake_path = Path("src/tests/fake")
    expected_result = (fake_path / "contacts-output.txt").read_text()
    output = StringIO()
    args = ["main.py", "john"]
    with (
        patch.object(sys, "argv", args),
        redirect_stdout(output),
    ):
        main()
    assert output.getvalue() == expected_result
