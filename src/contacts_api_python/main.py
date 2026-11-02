from fastapi import FastAPI

from contacts_api_python.cli import parse_arguments
from contacts_api_python.models import Contacts
from contacts_api_python.read import read_contacts
from contacts_api_python.representation import show_contacts
from contacts_api_python.search import search_contacts

app = FastAPI(title="Contacts API")


@app.get("/contacts")
def get_contacts(search_term: str | None = None) -> Contacts:
    contacts = read_contacts()
    if search_term:
        contacts = search_contacts(contacts, search_term)
    return contacts


def main() -> None:
    contacts = read_contacts()
    search_term = parse_arguments().search_term
    if search_term:
        contacts = search_contacts(contacts, search_term)
    show_contacts(contacts)


if __name__ == "__main__":
    main()
