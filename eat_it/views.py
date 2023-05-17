from flask import Flask, Response, request, jsonify
from flask.views import MethodView
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


class UserAPI(MethodView):
    def __init__(self, add_user_controller, delete_user_controller, update_user_controller, patch_user_controller, put_user_controller, get_user_controller):
        self.user_controller = UserRepository()
        self.add_user_controller = add_user_controller
        self.delete_user_controller = delete_user_controller
        self.update_user_controller = update_user_controller
        self.patch_user_controller = patch_user_controller
        self.put_user_controller = put_user_controller
        self.get_user_controller = get_user_controller

        

    def post(self):
        user = request.json
        self.add_user_controller.add(user)
        return jsonify(user), 201

    def get(self):
        return Response(status=501)

    def put(self, id):
        user = request.json
        self.put_user_controller.put(user)
        return jsonify(user), 200

    def patch(self, id):
        user = request.json
        self.patch_user_controller.patch(user)
        return jsonify(user), 200

    def delete(self, id):
        user = request.json
        self.delete_user_controller.delete(user)
        return Response(status=204)


user_view = UserAPI.as_view('user_api', add_user_controller=AddUserController(UserRepository()), delete_user_controller=DeleteUserController(UserRepository()), update_user_controller=UpdateUserController(UserRepository()), patch_user_controller=PatchUserController(UserRepository()), put_user_controller=PutUserController(UserRepository()), get_user_controller=GetUserController(UserRepository()))
app.add_url_rule('/users', view_func=user_view, methods=['POST', 'GET'])
app.add_url_rule('/users/<id>', view_func=user_view, methods=['PUT', 'PATCH', 'DELETE'])