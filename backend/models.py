from datetime import datetime
from extensions import db

class VPNUser(db.Model):
    __tablename__ = "vpn_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    enabled = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "enabled": self.enabled,
            "created_at": self.created_at.isoformat()
        }
