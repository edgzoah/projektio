from eat_it.app import app

UNIMPLEMENTED = 501


def test_app_has_ping_endpoint() -> None:
    client = app.test_client()
    response = client.get(path="/ping")
    assert response.status_code == UNIMPLEMENTED

def test_app_user_create_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 200

def test_app_user_get_endpoint() -> None:
    client = app.test_client()
    response = client.get(path='/users')
    assert response.status_code == UNIMPLEMENTED

def test_app_user_put_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.put(path='/users/1', json=payload)
    assert response.json == payload and response.status_code == 200

def test_app_user_patch_endpoint() -> None:
    payload = {"first_name": "Jan"}
    client = app.test_client()
    response = client.patch(path='/users/1', json=payload)
    assert response.json == payload and response.status_code == 200

def test_app_user_delete_endpoint() -> None:
    client = app.test_client()
    response = client.delete(path='/users/1')
    assert response.status_code == 204