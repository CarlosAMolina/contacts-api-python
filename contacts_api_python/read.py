from pathlib import Path

from contacts_api_python.models import Contacts
from contacts_api_python.models import ContactsFile


def read_contacts(json_path: Path) -> Contacts:
    if not json_path.is_file():
        raise FileNotFoundError(json_path)
    raw = json_path.read_text()
    return ContactsFile.model_validate_json(raw).contacts
