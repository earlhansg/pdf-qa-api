from flask import Blueprint, request, jsonify
from models import db, Knowledge

knowledge_bp = Blueprint('knowledge', __name__)

@knowledge_bp.route('/knowledge', methods=['POST'])
def add_knowledge():
    data = request.get_json()
    new_knowledge = Knowledge(title=data['title'], content=data['content'])
    db.session.add(new_knowledge)
    db.session.commit()
    return jsonify({"message": "Knowledge added"}), 201