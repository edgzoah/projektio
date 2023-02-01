from eat_it.app import ping, create_user, app, get_users, update_user, patch_user, delete_user

UNIMPLEMENTED = 501


def test_ping_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED


def test_create_user_returns_user() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = create_user()
    assert result.json == payload

def test_users_get_returns_501_response() -> None:
    with app.test_request_context(method="GET", path="/users"):
        result = get_users()
    assert result.status_code == UNIMPLEMENTED

def test_users_put_returns_user() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    with app.test_request_context(method="PUT", path="/users/1", json=payload):
        result = update_user(id="1")
    assert result.json == payload and result.status_code == 200

def test_users_patch_returns_user() -> None:
    payload = {"first_name": "Jan"}
    with app.test_request_context(method="PATCH", path="/users/1", json=payload):
        result = patch_user(id="1")
    assert result.json == payload and result.status_code == 200

def test_users_delete_returns_204_response() -> None:
    with app.test_request_context(method="DELETE", path="/users/1"):
        result = delete_user(id="1")
    assert result.status_code == 204