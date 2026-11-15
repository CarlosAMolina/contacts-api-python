from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from contacts_api_python.constants import DESCRIPTION
from contacts_api_python.exceptions import ContactNotFoundError
from contacts_api_python.routers import contacts

app = FastAPI(
    title=DESCRIPTION,
    description="An API for managing contacts that are typically stored in a mobile phone’s address book.",
)

app.include_router(contacts.router)


@app.exception_handler(ContactNotFoundError)
def handle_contact_not_found_error(request: Request, exc: ContactNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Contact not found"},
    )


@app.exception_handler(FileNotFoundError)
def handle_file_not_found_error(request: Request, exc: FileNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"detail": "No contacts file"},
    )


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "app": DESCRIPTION,
        "docs": "/docs",
    }
