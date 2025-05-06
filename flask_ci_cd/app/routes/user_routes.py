from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from ..services.user_service import fetch_users
from ..rabbit.send_task import send_task_to_process_data

from ..models import db, User

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/", methods=['GET'])
def home():
    return jsonify(message="Flask API working")

@api_blueprint.route('/users', methods=['GET'])
def get_users():
    try:
        user_data = fetch_users()
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@api_blueprint.route("/process_user", methods=['GET'])
def process_user():
    try:
        data = request.get_json()
        print(f"Request body {data}")
        batch_data = [{"user_id": i, "data": f'user_data_{i}'} for i in data['ids']]
        send_task_to_process_data(batch_data)
        return jsonify(
            {"message":f"Task sent for user id {data}"},
            ), 202
    except Exception as e:
        return jsonify({
            "error": f"Error sending task to Rabbit queue {str(e)}"
        }), 500
 