from flask import Flask, jsonify, request
from config import Config
from extensions import db
from models import VPNUser
from mikrotik_client import MikrotikClient

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    mikrotik = MikrotikClient(
        host=app.config.get("MIKROTIK_HOST"),
        port=app.config.get("MIKROTIK_PORT"),
        username=app.config.get("MIKROTIK_USER"),
        password=app.config.get("MIKROTIK_PASSWORD"),
    )

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/api/users", methods=["GET"])
    def list_users():
        users = VPNUser.query.all()
        return jsonify([u.to_dict() for u in users]), 200

    @app.route("/api/users", methods=["POST"])
    def create_user():
        data = request.get_json() or {}
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "username and password required"}), 400

        if VPNUser.query.filter_by(username=username).first():
            return jsonify({"error": "username already exists"}), 409

        user = VPNUser(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        if mikrotik.is_configured():
            mikrotik.create_vpn_user(username, password)

        return jsonify(user.to_dict()), 201

    @app.route("/api/users/<int:user_id>/disable", methods=["POST"])
    def disable_user(user_id):
        user = VPNUser.query.get_or_404(user_id)
        user.enabled = False
        db.session.commit()

        if mikrotik.is_configured():
            mikrotik.disable_vpn_user(user.username)

        return jsonify(user.to_dict()), 200

    @app.route("/api/users/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        user = VPNUser.query.get_or_404(user_id)

        if mikrotik.is_configured():
            mikrotik.delete_vpn_user(user.username)

        db.session.delete(user)
        db.session.commit()
        return jsonify({"status": "deleted"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
