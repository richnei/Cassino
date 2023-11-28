from typing import Generator
from fastapi.testclient import TestClient
import pytest
from app import app

@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c