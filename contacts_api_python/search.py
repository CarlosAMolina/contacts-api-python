from typing import Any

from contacts_api_python.models import Contact
from contacts_api_python.models import Contacts


def search_contacts(contacts: Contacts, term: str) -> Contacts:
    term = term.lower()
    return [contact for contact in contacts if _has_term(contact, term)]


def _has_term(contact: Contact, term: str) -> bool:
    return _contains_term(contact.model_dump(exclude_none=True), term)


def _contains_term(value: Any, term: str) -> bool:
    if isinstance(value, dict):
        return any(
            _contains_term(value_in_mapping, term)
            for value_in_mapping in value.values()
        )
    elif isinstance(value, (list, tuple)):
        return any(_contains_term(item, term) for item in value)
    return term in str(value).lower()
