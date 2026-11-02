import json

from contacts_api_python.models import Contacts


def show_contacts(contacts: Contacts) -> None:
    print(
        json.dumps(
            [contact.model_dump(exclude_none=True) for contact in contacts],
            indent=2,
            ensure_ascii=False,
        )
    )
