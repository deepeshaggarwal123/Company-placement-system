# backend/models/role.py

from extensions import db
from flask_security import RoleMixin

# -------------------------------------------------
# Association Table (Many-to-Many)
# -------------------------------------------------
roles_users = db.Table(
    "roles_users",

    db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("users.id"),
        primary_key=True
    ),

    db.Column(
        "role_id",
        db.Integer,
        db.ForeignKey("roles.id"),
        primary_key=True
    )
)


# -------------------------------------------------
# Role Model
# -------------------------------------------------
class Role(db.Model, RoleMixin):
    __tablename__ = "roles"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.String(255),
        nullable=True
    )

    # Relationship with User
    users = db.relationship(
        "User",
        secondary=roles_users,
        back_populates="roles",
        lazy="dynamic"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    def __repr__(self):
        return f"<Role {self.name}>"