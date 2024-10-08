from collections.abc import Generator

from fastapi.testclient import TestClient
from pytest import fixture

from main import app
from models import CreateUser


@fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    """Fixture to create teste cliente per module."""
    with TestClient(app) as client:
        yield client


def test_create_user(client: TestClient):
    test_user = CreateUser(
        username="himynameis", password="whatmynameis"
    ).model_dump_json()
    response = client.post("/users/", json=test_user)

    assert response.status_code == 200
