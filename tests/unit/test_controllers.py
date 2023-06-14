import json
from unittest.mock import Mock
import pytest
from _pytest.capture import CaptureFixture
from eat_it.controllers import AddUserController, UserRequest, DeleteUserController, UpdateUserController, GetUserController, GetUsersController
from eat_it.repositories import UserRepository

@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}

@pytest.fixture
def user_repository() -> UserRepository:
    return Mock(UserRepository)

@pytest.fixture
def controller(user_repository: UserRepository) -> AddUserController:
    return AddUserController(repository=user_repository)

def test_add_user_controller_has_add_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: AddUserController,
) -> None:
    request = UserRequest(user=payload)
    controller.add(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

def test_calls_add_in_repository_on_calling_controller(
        controller: AddUserController,
        user_repository: Mock,
        payload: dict,
) -> None:
    request = UserRequest(user=payload)
    controller.add(request)
    assert user_repository.add.call_count > 0

def test_add_user_request_has_user_attribute(payload: dict) -> None:
    request = UserRequest(user=payload)
    assert request.user
 
def test_delete_user_controller_has_delete_method(
    capsys: CaptureFixture,
    controller: DeleteUserController,
) -> None:
    request = UserRequest(user=payload)
    controller.delete(request)
    actual = capsys.readouterr().out
    expected = f"\n".replace('"', "'")
    assert actual == expected

def test_calls_delete_in_repository_on_calling_controller(
        controller: DeleteUserController,
) -> None:
    request = UserRequest(user=payload)
    controller.delete(request)
    assert user_repository.delete.call_count > 0

def test_delete_user_request_has_user_id_attribute(user_id: str) -> None:
    request = UserRequest(user_id=user_id)
    assert request.user

def test_update_user_controller_has_update_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: UpdateUserController,
) -> None:
    request =UserRequest(user=payload)
    controller.update(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

def test_calls_update_in_repository_on_calling_controller(
        controller: UpdateUserController,
        payload: dict,
) -> None:
    request = UserRequest(user=payload)
    controller.update(request)
    assert user_repository.update.call_count > 0

def test_update_user_request_has_user_id_and_user_attribute(user_id: str, payload: dict) -> None:
    request = UserRequest(user_id=user_id, user=payload)
    assert request.user

def test_put_user_controller_has_put_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: PutUserController,
) -> None:
    request =UserRequest(user=payload)
    controller.put(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

def test_calls_put_in_repository_on_calling_controller(
        controller: PutUserController,
        user_id: str,
        payload: dict,
) -> None:
    request = UserRequest(user_id=user_id, user=payload)
    controller.put(request)
    assert user_repository.put.call_count > 0

def test_put_user_request_has_user_id_and_user_attribute(user_id: str, payload: dict) -> None:
    request = UserRequest(user_id=user_id, user=payload)
    assert request.user

def test_get_user_controller_has_get_method(
    capsys: CaptureFixture,
    user_id: str,
    controller: GetUserController,
) -> None:
    request = UserRequest(user_id=user_id)
    controller.get(request)
    actual = capsys.readouterr().out
    expected = f"{user_id}\n".replace('"', "'")
    assert actual == expected

def test_calls_get_in_repository_on_calling_controller(
        controller: GetUserController,
        user_id: str,
) -> None:
    request = UserRequest(user_id=user_id)
    controller.get(request)
    assert user_repository.get.call_count > 0

def test_get_user_request_has_user_id_attribute(payload: dict) -> None:
    request = UserRequest(user=payload)
    assert request.user