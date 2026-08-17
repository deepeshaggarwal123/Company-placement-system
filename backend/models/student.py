# backend/models/student.py

from datetime import datetime
from extensions import db


class Student(db.Model):
    __tablename__ = "students"

    # -----------------------------------
    # Primary Key
    # -----------------------------------
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # -----------------------------------
    # User Relationship (One-to-One)
    # -----------------------------------
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    # -----------------------------------
    # Personal Details
    # -----------------------------------
    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    enrollment_no = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(15),
        nullable=False
    )

    gender = db.Column(
        db.String(20),
        nullable=True
    )

    date_of_birth = db.Column(
        db.Date,
        nullable=True
    )

    # -----------------------------------
    # Academic Details
    # -----------------------------------
    branch = db.Column(
        db.String(100),
        nullable=False
    )

    year = db.Column(
        db.Integer,
        nullable=False
    )

    cgpa = db.Column(
        db.Float,
        nullable=False
    )

    university = db.Column(
        db.String(150),
        nullable=True
    )

    # -----------------------------------
    # Resume & Skills
    # -----------------------------------
    resume = db.Column(
        db.String(255),
        nullable=True
    )

    skills = db.Column(
        db.Text,
        nullable=True
    )

    address = db.Column(
        db.Text,
        nullable=True
    )

    profile_image = db.Column(
        db.String(255),
        nullable=True
    )

    # -----------------------------------
    # Status
    # -----------------------------------
    is_active = db.Column(
        db.Boolean,
        default=True
    )

    is_blacklisted = db.Column(
        db.Boolean,
        default=False
    )

    # -----------------------------------
    # Timestamp
    # -----------------------------------
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # -----------------------------------
    # Relationships
    # -----------------------------------

    user = db.relationship(
        "User",
        back_populates="student",
        uselist=False
    )

    applications = db.relationship(
        "Application",
        back_populates="student",
        cascade="all, delete-orphan",
        lazy=True
    )

    # -----------------------------------
    # Helper Methods
    # -----------------------------------

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name": self.full_name,
            "enrollment_no": self.enrollment_no,
            "email": self.email,
            "phone": self.phone,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth.strftime("%Y-%m-%d")
            if self.date_of_birth else None,
            "branch": self.branch,
            "year": self.year,
            "cgpa": self.cgpa,
            "university": self.university,
            "resume": self.resume,
            "skills": self.skills,
            "address": self.address,
            "profile_image": self.profile_image,
            "is_active": self.is_active,
            "is_blacklisted": self.is_blacklisted,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
            if self.created_at else None,
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            if self.updated_at else None,
        }

    def __repr__(self):
        return f"<Student {self.full_name}>"