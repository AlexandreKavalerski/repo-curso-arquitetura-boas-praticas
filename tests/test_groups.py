def test_create_group(client):
    response = client.post("/api/v1/groups/", json={"name": "Pelada da Sexta"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Pelada da Sexta"
    assert "id" in data


def test_list_groups_empty(client):
    response = client.get("/api/v1/groups/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_group_by_id(client):
    created = client.post("/api/v1/groups/", json={"name": "Pelada"}).json()
    response = client.get(f"/api/v1/groups/{created['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Pelada"


def test_get_group_not_found(client):
    response = client.get("/api/v1/groups/999")
    assert response.status_code == 404
