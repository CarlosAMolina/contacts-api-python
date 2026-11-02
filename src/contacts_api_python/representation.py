import json

from contacts_api_python.models import Contacts


def prettify_contacts(contacts: Contacts) -> str:
    data = [contact.model_dump(exclude_none=True) for contact in contacts]
    return json.dumps(
        data,
        ensure_ascii=False,
        indent=2,
    )
