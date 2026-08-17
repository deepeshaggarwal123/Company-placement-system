# backend/models/company.py

from datetime import datetime
from extensions import db


class Company(db.Model):
    __tablename__ = "companies"

    # ----------------------------
    # Primary Key
    # ----------------------------
    id = db.Column(db.Integer, primary_key=True)

    # ----------------------------
    # User Relationship
    # ----------------------------
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    # ----------------------------
    # Company Details
    # ----------------------------
    company_name = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    website = db.Column(
        db.String(255),
        nullable=True
    )

    hr_name = db.Column(
        db.String(100),
        nullable=False
    )

    hr_email = db.Column(
        db.String(120),
        nullable=False,
        unique=True
    )

    hr_phone = db.Column(
        db.String(20),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    industry = db.Column(
        db.String(100),
        nullable=True
    )

    address = db.Column(
        db.Text,
        nullable=True
    )

    logo = db.Column(
        db.String(255),
        nullable=True
    )

    # ----------------------------
    # Approval & Status
    # ----------------------------
    approval_status = db.Column(
        db.String(20),
        default="Pending",
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    is_blacklisted = db.Column(
        db.Boolean,
        default=False
    )

    # ----------------------------
    # Timestamp
    # ----------------------------
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # ----------------------------
    # Relationships
    # ----------------------------

    # User Profile
    user = db.relationship(
        "User",
        back_populates="company",
        uselist=False
    )

    # Placement Drives
    drives = db.relationship(
        "PlacementDrive",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    # ----------------------------
    # Helper Methods
    # ----------------------------

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "company_name": self.company_name,
            "website": self.website,
            "hr_name": self.hr_name,
            "hr_email": self.hr_email,
            "hr_phone": self.hr_phone,
            "description": self.description,
            "industry": self.industry,
            "address": self.address,
            "logo": self.logo,
            "approval_status": self.approval_status,
            "is_active": self.is_active,
            "is_blacklisted": self.is_blacklisted,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
            if self.created_at else None
        }

    def __repr__(self):
        return f"<Company {self.company_name}>"