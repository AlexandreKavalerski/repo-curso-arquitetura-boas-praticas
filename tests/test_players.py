def test_create_player(client):
    response = client.post(
        "/api/v1/players/", json={"name": "João Silva", "phone": "11999990000"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "João Silva"
    assert data["phone"] == "11999990000"
    assert "id" in data
    assert "created_at" in data


def test_list_players_empty(client):
    response = client.get("/api/v1/players/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_player_by_id(client):
    created = client.post("/api/v1/players/", json={"name": "Maria"}).json()
    response = client.get(f"/api/v1/players/{created['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Maria"


def test_get_player_not_found(client):
    response = client.get("/api/v1/players/999")
    assert response.status_code == 404
