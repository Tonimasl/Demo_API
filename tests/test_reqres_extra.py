import time
import pytest

def test_user_response_structure(client):
    response = client.get("/users?page=1")
    assert response.status_code == 200
    users = response.json()["data"]
    assert isinstance(users, list)
    for user in users:
        assert isinstance(user, dict)
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user

def test_resource_response_structure(client):
    response = client.get("/unknown")
    assert response.status_code == 200
    for item in response.json()["data"]:
        assert "id" in item
        assert "name" in item
        assert "year" in item
        assert "color" in item
        assert "pantone_value" in item

def test_response_time_users(client):
    start = time.time()
    response = client.get("/users")
    end = time.time()
    assert response.status_code == 200
    assert (end - start) < 1.0  # ответ должен быть менее 1 секунды

def test_not_allowed_method_on_login(client):
    response = client.put("/login", json={"email": "eve.holt@reqres.in"})
    assert response.status_code in (400, 404, 405)

def test_register_with_empty_body(client):
    response = client.post("/register", json={})
    assert response.status_code == 400
    assert "error" in response.json()

def test_login_with_empty_body(client):
    response = client.post("/login", json={})
    assert response.status_code == 400
    assert "error" in response.json()

@pytest.mark.parametrize("endpoint", ["/users", "/unknown"])
def test_get_collection_has_non_empty_data(client, endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200
    data = response.json().get("data", [])
    assert isinstance(data, list)
    assert len(data) > 0
