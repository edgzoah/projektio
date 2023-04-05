from flask import Flask, Response, request, jsonify
from eat_it.repositories import UserRepository
from eat_it.controllers import (
    AddUserController,
    DeleteUserController,
    UpdateUserController,
    PatchUserController,
    PutUserController,
    GetUserController,
)

app = Flask(__name__)

@app.get('/')
def index():
    return 'Hello, World!'

@app.get("/ping")
def ping():
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    controller = AddUserController(UserRepository())
    controller.add(user)
    return jsonify(user)

@app.get('/users')
def get_users() -> Response:
    return Response(status=501)

@app.put('/users/<id>')
def update_user(id: str) -> Response:
    user = request.json
    controller = UpdateUserController(UserRepository())
    controller.update(user)
    return jsonify(user)

@app.patch('/users/<id>')
def patch_user(id: str) -> Response:
    user = request.json
    controller = PatchUserController(UserRepository())
    controller.patch(user)
    return jsonify(user)

@app.delete('/users/<id>')
def delete_user(id: str) -> Response:
    user = request.json
    controller = DeleteUserController(UserRepository())
    controller.delete(user)
    return Response(status=204)