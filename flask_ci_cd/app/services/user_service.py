import requests
from flask import current_app, jsonify

def fetch_users():
    try:
        response = requests.get(current_app.config['USER_SERVICE_URL'])
        response.raise_for_status()
        user_data = response.json()
        # users = User.query.all()
        # return jsonify(users=[user.to_dict() for user in users])
        return user_data, 200
    except requests.exceptions.RequestException as e:
        # return jsonify({"message": f"Error fetching users from user service: {str(e)}"}), 500
        current_app.logger.error(f"Error fetching users: {e}")
        raise

