def test_create_game(client):
    response = client.post(
        "/api/v1/games/",
        json={"played_at": "2026-05-24T10:00:00Z", "location": "Quadra do Parque"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["location"] == "Quadra do Parque"
    assert "id" in data


def test_list_games_empty(client):
    response = client.get("/api/v1/games/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_game_by_id(client):
    created = client.post(
        "/api/v1/games/", json={"played_at": "2026-05-24T10:00:00Z", "location": "Quadra A"}
    ).json()
    response = client.get(f"/api/v1/games/{created['id']}")
    assert response.status_code == 200
    assert response.json()["location"] == "Quadra A"


def test_get_game_not_found(client):
    response = client.get("/api/v1/games/999")
    assert response.status_code == 404
