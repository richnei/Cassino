from fastapi.testclient import TestClient

def test_post_bet(client: TestClient) -> None:
    response = client.post("/bet", json={"player": 1, "value": 5})
    assert response.status_code == 200
    assert response.json()["player"] == 1
    assert response.json()["balance"] == 995
    assert "txn" in response.json()
