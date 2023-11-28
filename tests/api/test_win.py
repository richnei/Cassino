from fastapi.testclient import TestClient

def test_post_win(client: TestClient) -> None:
     response = client.post("/win", json={"player": 1, "value": 1000})
     assert response.status_code == 200
     assert response.json()["player"] == 1
     assert response.json()["balance"] == 1995
     assert "txn" in response.json()

def test_post_win_player_not_exist(client: TestClient) -> None:
    response = client.post("/win", json={"player": 99, "value": 100})
    assert response.status_code == 400
    assert response.json()["detail"] == "Player não existe"


