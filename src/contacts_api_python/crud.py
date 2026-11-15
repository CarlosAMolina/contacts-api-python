from contacts_api_python.json_file.read import read_contacts
from contacts_api_python.json_file.search import search_contacts
from contacts_api_python.models import Contact
from contacts_api_python.models import Contacts


def list_contacts(search_term: str | None = None) -> Contacts:
    contacts = read_contacts()
    if search_term:
        contacts = search_contacts(contacts, search_term)
    return contacts


def get_contact(contact_id: int) -> Contact | None:
    contacts = read_contacts()
    for contact in contacts:
        if contact.id == contact_id:
            return contact
    return None
