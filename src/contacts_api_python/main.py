from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import Response

from contacts_api_python import crud
from contacts_api_python.models import Contact
from contacts_api_python.models import Contacts

_TITLE = "Contacts API"

app = FastAPI(
    title=_TITLE,
    description="An API for managing contacts that are typically stored in a mobile phone’s address book.",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "app": _TITLE,
        "docs": "/docs",
    }


@app.get("/contacts")
def get_contacts(search_term: str | None = None) -> Contacts:
    return crud.list_contacts(search_term)


@app.get("/contacts/html")
def get_contacts_html(search_term: str | None = None) -> Response:
    content = crud.list_contacts_html(search_term)
    return Response(
        content=content,
        media_type="application/json",
    )


@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int) -> Contact:
    if contact := crud.get_contact(contact_id):
        return contact
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
    )
