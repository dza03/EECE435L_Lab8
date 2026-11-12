from flask import Flask, jsonify
from database import init_db, get_users

app = Flask(__name__)


@app.route('/api/get_users', methods=['GET'])
def api_get_users():
    users = get_users()
    names = [user["name"] for user in users]
    return jsonify(names)


if __name__ == "__main__":
    init_db()
    # host 0.0.0.0 so the app can be reached from outside the container
    app.run(host="0.0.0.0", port=3000)
