import pytest
from eat_it.repositories import UserRepository

@pytest.fixture
def repository() -> UserRepository:
    return UserRepository()

def test_can_instantiate_user_repository(
    repository: UserRepository,
) -> None:
    pass

def test_raises_on_add_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.add()

def test_raises_on_delete_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.delete()

def test_raises_on_update_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.update()

def test_raises_on_patch_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.patch()

def test_raises_on_put_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.put()