from typing import Annotated

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import StringConstraints


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ContactsFile(_StrictModel):
    contacts: Contacts


type Contacts = list[Contact]


class Contact(_StrictModel):
    addresses: list[str] | None = None
    categories: list[str] | None = None
    emails: list[str] | None = None
    id: _PositiveInt
    name: _ContactName
    nicknames: list[str] | None = None
    note: str | None = None
    phones: list[_Phone] | None = None
    socialNetwork: _SocialNetwork | None = None
    surname: str | None = None
    urls: list[str] | None = None


_ContactName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1),
]

_PositiveInt = Annotated[int, Field(gt=0)]


class _Phone(_StrictModel):
    description: str | None = None
    number: str


class _SocialNetwork(_StrictModel):
    discordAccounts: list[_DiscordAccounts] | None = None
    facebookAccounts: list[str] | None = None
    githubAccounts: list[str] | None = None
    instagramAccounts: list[str] | None = None
    linkedinAccounts: list[str] | None = None
    telegramAccounts: list[str] | None = None
    tiktokAccounts: list[str] | None = None
    twitterAccounts: list[str] | None = None
    wallapopAccounts: list[_WallapopAccounts] | None = None


class _DiscordAccounts(_StrictModel):
    alias: str
    discriminator: int | None = None
    globalName: str | None = None
    legacyUserName: str | None = None
    userName: str


class _WallapopAccounts(_StrictModel):
    url: str
    note: str
