def test_get_users_page_2(client):
    response = client.get("/users?page=2")
    assert response.status_code == 200
    json_data = response.json()
    assert "page" in json_data and json_data["page"] == 2
    assert isinstance(json_data.get("data"), list)

def test_get_single_user_exists(client):
    response = client.get("/users/2")
    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"]["id"] == 2

def test_get_single_user_not_found(client):
    response = client.get("/users/23")
    assert response.status_code == 404

def test_list_resource(client):
    response = client.get("/unknown")
    assert response.status_code == 200
    assert isinstance(response.json().get("data"), list)

def test_single_resource_exists(client):
    response = client.get("/unknown/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_single_resource_not_found(client):
    response = client.get("/unknown/23")
    assert response.status_code == 404

def test_create_user(client):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "morpheus"
    assert json_data["job"] == "leader"
    assert "id" in json_data
    assert "createdAt" in json_data

def test_update_user_put(client):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = client.put("/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"

def test_update_user_patch(client):
    payload = {
        "job": "the one"
    }
    response = client.patch("/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "the one"

def test_delete_user(client):
    response = client.delete("/users/2")
    assert response.status_code == 204
    assert response.text == ""

def test_register_successful(client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()

def test_register_unsuccessful_missing_password(client):
    payload = {
        "email": "sydney@fife"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()

def test_login_successful(client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_unsuccessful_missing_password(client):
    payload = {
        "email": "peter@klaven"
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()

def test_delayed_response(client):
    response = client.get("/users?delay=3")
    assert response.status_code == 200
    assert "data" in response.json()
