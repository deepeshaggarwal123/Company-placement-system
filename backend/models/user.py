# backend/models/user.py

from datetime import datetime

from flask_security import UserMixin
from extensions import db
from models.role import roles_users


class User(db.Model, UserMixin):
    __tablename__ = "users"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # ---------------------------------
    # Login Credentials
    # ---------------------------------
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        default=True
    )

    fs_uniquifier = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    # ---------------------------------
    # Role
    # ---------------------------------
    roles = db.relationship(
        "Role",
        secondary=roles_users,
        back_populates="users",
        lazy="joined"
    )

    # ---------------------------------
    # Student Profile
    # ---------------------------------
    student = db.relationship(
        "Student",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # ---------------------------------
    # Company Profile
    # ---------------------------------
    company = db.relationship(
        "Company",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # ---------------------------------
    # Timestamp
    # ---------------------------------
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # ---------------------------------
    # Helper Methods
    # ---------------------------------
    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles)

    @property
    def role(self):
        if self.roles:
            return self.roles[0].name
        return None

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "role": self.role,
            "active": self.active,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
            if self.created_at else None,
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            if self.updated_at else None,
        }

    def __repr__(self):
        return f"<User {self.email}>"