from dataclasses import dataclass
from eat_it.repositories import UserRepository

@dataclass
class UserRequest:
    user: dict

class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def add(self, request: UserRequest) -> None:
        print(request.user)

class DeleteUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def delete(self, request: UserRequest) -> None:
        print(request.user)

class UpdateUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def update(self, request: UserRequest) -> None:
        print(request.user)

class PatchUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def patch(self, request: UserRequest) -> None:
        print(request.user)

class PutUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def put(self, request: UserRequest) -> None:
        print(request.user)

class GetUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def get(self, request: UserRequest) -> None:
        print(request.user)