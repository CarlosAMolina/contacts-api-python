import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from contacts_api_python.main import main


def test_main_shows_contacts():
    fake_path = Path("tests/fake")
    json_path = fake_path / "contacts.json"
    expected_result = (fake_path / "contacts-output.txt").read_text()
    output = StringIO()
    args = ["main.py", str(json_path), "john"]
    with (
        patch.object(sys, "argv", args),
        redirect_stdout(output),
    ):
        main()
    assert output.getvalue() == expected_result
