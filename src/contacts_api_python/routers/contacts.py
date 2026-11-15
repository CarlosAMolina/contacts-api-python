from fastapi import APIRouter
from fastapi.responses import Response

from contacts_api_python.dependencies import ContactDep
from contacts_api_python.dependencies import ContactsDep
from contacts_api_python.models import Contact
from contacts_api_python.models import Contacts
from contacts_api_python.representation import prettify_contacts

# tags: to group similarly tagged objects together in the docs view.
router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/")
def get_contacts(contacts: ContactsDep) -> Contacts:
    return contacts


@router.get("/html")
def get_contacts_html(contacts: ContactsDep) -> Response:
    content = prettify_contacts(contacts)
    return Response(
        content=content,
        media_type="application/json",
    )


@router.get("/{contact_id}")
def get_contact(contact: ContactDep) -> Contact:
    return contact
