from dataclasses import dataclass
from eat_it.repositories import UserRepository

@dataclass
class UserRequest:
    user: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def add(self, request: UserRequest) -> None:
        return NotImplemented


class DeleteUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def delete(self, request: UserRequest) -> None:
        return NotImplemented


class UpdateUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def update(self, request: UserRequest) -> None:
        return NotImplemented

class PatchUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def patch(self, request: UserRequest) -> None:
        return NotImplemented


class PutUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def put(self, request: UserRequest) -> None:
        return NotImplemented

class GetUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def get(self, request: UserRequest) -> None:
        return NotImplemented