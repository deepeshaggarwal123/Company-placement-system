# backend/models/drive.py

from datetime import datetime
from extensions import db


class PlacementDrive(db.Model):
    __tablename__ = "placement_drives"

    # -----------------------------
    # Primary Key
    # -----------------------------
    id = db.Column(db.Integer, primary_key=True)

    # -----------------------------
    # Company Relationship
    # -----------------------------
    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False
    )

    # -----------------------------
    # Job Details
    # -----------------------------
    job_title = db.Column(
        db.String(150),
        nullable=False
    )

    job_description = db.Column(
        db.Text,
        nullable=False
    )

    job_location = db.Column(
        db.String(100),
        nullable=True
    )

    job_type = db.Column(
        db.String(50),
        nullable=True
    )  # Full-Time / Internship

    package = db.Column(
        db.Float,
        nullable=True
    )

    vacancies = db.Column(
        db.Integer,
        default=1
    )

    # -----------------------------
    # Eligibility
    # -----------------------------
    eligible_branch = db.Column(
        db.String(100),
        nullable=False
    )

    minimum_cgpa = db.Column(
        db.Float,
        default=0.0
    )

    eligible_year = db.Column(
        db.Integer,
        nullable=False
    )

    # -----------------------------
    # Dates
    # -----------------------------
    application_deadline = db.Column(
        db.Date,
        nullable=False
    )

    drive_date = db.Column(
        db.Date,
        nullable=True
    )

    # -----------------------------
    # Status
    # -----------------------------
    status = db.Column(
        db.String(20),
        default="Pending",
        nullable=False
    )
    # Pending / Approved / Rejected / Closed

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    # -----------------------------
    # Timestamp
    # -----------------------------
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # -----------------------------
    # Relationships
    # -----------------------------
    company = db.relationship(
        "Company",
        back_populates="drives"
    )

    applications = db.relationship(
        "Application",
        back_populates="drive",
        cascade="all, delete-orphan"
    )

    # -----------------------------
    # Helper Methods
    # -----------------------------
    def to_dict(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "job_title": self.job_title,
            "job_description": self.job_description,
            "job_location": self.job_location,
            "job_type": self.job_type,
            "package": self.package,
            "vacancies": self.vacancies,
            "eligible_branch": self.eligible_branch,
            "minimum_cgpa": self.minimum_cgpa,
            "eligible_year": self.eligible_year,
            "application_deadline": (
                self.application_deadline.strftime("%Y-%m-%d")
                if self.application_deadline else None
            ),
            "drive_date": (
                self.drive_date.strftime("%Y-%m-%d")
                if self.drive_date else None
            ),
            "status": self.status,
            "is_active": self.is_active,
            "created_at": (
                self.created_at.strftime("%Y-%m-%d %H:%M:%S")
                if self.created_at else None
            ),
        }

    def __repr__(self):
        return (
            f"<PlacementDrive "
            f"{self.job_title} - {self.company.company_name}>"
        )