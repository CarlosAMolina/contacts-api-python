from pathlib import Path

from fastapi.testclient import TestClient

from contacts_api_python.main import app

client = TestClient(app)


def test_get_contacts_if_no_search_term(contacts_path_env_fixture):
    response = client.get("/contacts")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_contacts_if_search_term(contacts_path_env_fixture):
    response = client.get("/contacts", params={"search_term": "john"})
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_contacts_html_has_expected_content(contacts_path_env_fixture):
    response = client.get("/contacts/html", params={"search_term": "john"})
    fake_path = Path("tests/fake")
    expected_result = (fake_path / "contacts-output.txt").read_text()
    assert response.content == expected_result.strip().encode("utf-8")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200


def test_get_contact_if_contact_id_exists(contacts_path_env_fixture):
    response = client.get("/contacts/1")
    assert response.status_code == 200


def test_get_contact_if_contact_id_does_not_exist(contacts_path_env_fixture):
    response = client.get("/contacts/-1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Contact not found"}
