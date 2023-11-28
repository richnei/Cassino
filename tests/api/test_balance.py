from fastapi.testclient import TestClient

def test_get_balance(client: TestClient) -> None:
    response = client.get("/balance?player=1")
    assert response.status_code == 200
    assert response.json() == {"player": 1, "balance": 1000}

