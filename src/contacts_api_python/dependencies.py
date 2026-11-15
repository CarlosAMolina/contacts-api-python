from typing import Annotated

from fastapi import Depends

from contacts_api_python import crud
from contacts_api_python.exceptions import ContactNotFoundError
from contacts_api_python.models import Contact
from contacts_api_python.models import Contacts


def _get_contact(contact_id: int) -> Contact:
    if contact := crud.get_contact(contact_id):
        return contact
    raise ContactNotFoundError()


def _get_contacts(search_term: str | None = None) -> Contacts:
    return crud.list_contacts(search_term)


ContactDep = Annotated[Contact, Depends(_get_contact)]
ContactsDep = Annotated[Contacts, Depends(_get_contacts)]
