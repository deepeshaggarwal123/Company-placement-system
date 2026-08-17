# backend/models/application.py

from datetime import datetime
from extensions import db


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    # Foreign Keys
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    drive_id = db.Column(
        db.Integer,
        db.ForeignKey("placement_drives.id"),
        nullable=False
    )

    # Application Details
    application_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Applied"
    )

    interview_date = db.Column(
        db.DateTime,
        nullable=True
    )

    remarks = db.Column(
        db.Text,
        nullable=True
    )

    # Relationships
    student = db.relationship(
        "Student",
        back_populates="applications"
    )

    drive = db.relationship(
        "PlacementDrive",
        back_populates="applications"
    )

    # Prevent duplicate applications
    __table_args__ = (
        db.UniqueConstraint(
            "student_id",
            "drive_id",
            name="unique_student_drive"
        ),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "drive_id": self.drive_id,
            "application_date": self.application_date.strftime("%Y-%m-%d %H:%M:%S")
            if self.application_date else None,
            "status": self.status,
            "interview_date": self.interview_date.strftime("%Y-%m-%d %H:%M:%S")
            if self.interview_date else None,
            "remarks": self.remarks
        }

    def __repr__(self):
        return (
            f"<Application "
            f"Student={self.student_id} "
            f"Drive={self.drive_id} "
            f"Status={self.status}>"
        )