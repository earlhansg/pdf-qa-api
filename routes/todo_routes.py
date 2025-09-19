from flask import Blueprint, request, jsonify
from models.todo_model import Todo
from db import db

todo_bp = Blueprint("todo_bp", __name__)

@todo_bp.route("/", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@todo_bp.route("/", methods=["POST"])
def create_todo():
    data = request.get_json()
    new_todo = Todo(task=data.get("task", ""))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

@todo_bp.route("/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()
    todo.task = data.get("task", todo.task)
    todo.done = data.get("done", todo.done)
    db.session.commit()
    return jsonify(todo.to_dict())

@todo_bp.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted"})
