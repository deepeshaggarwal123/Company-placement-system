# backend/services/application_service.py

from datetime import datetime

from extensions import db
from models.application import Application
from models.student import Student
from models.drive import PlacementDrive


class ApplicationService:

    @staticmethod
    def apply(student_user_id, drive_id):
        """
        Student applies for a placement drive.
        """

        student = Student.query.filter_by(
            user_id=student_user_id
        ).first()

        if student is None:
            return False, "Student not found."

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Placement Drive not found."

        if drive.status != "Approved":
            return False, "Drive is not approved."

        if not drive.is_active:
            return False, "Drive is closed."

        # Eligibility Check

        if student.branch != drive.eligible_branch:
            return False, "Branch not eligible."

        if student.cgpa < drive.minimum_cgpa:
            return False, "CGPA requirement not met."

        if student.year != drive.eligible_year:
            return False, "Year not eligible."

        # Duplicate Check

        exists = Application.query.filter_by(
            student_id=student.id,
            drive_id=drive.id
        ).first()

        if exists:
            return False, "Already applied."

        application = Application(
            student_id=student.id,
            drive_id=drive.id,
            application_date=datetime.utcnow(),
            status="Applied"
        )

        db.session.add(application)
        db.session.commit()

        return True, application

    @staticmethod
    def get_student_applications(student_user_id):

        student = Student.query.filter_by(
            user_id=student_user_id
        ).first()

        if student is None:
            return []

        return Application.query.filter_by(
            student_id=student.id
        ).all()

    @staticmethod
    def get_drive_applications(drive_id):

        return Application.query.filter_by(
            drive_id=drive_id
        ).all()

    @staticmethod
    def update_status(application_id, status):

        application = Application.query.get(application_id)

        if application is None:
            return False, "Application not found."

        allowed = [
            "Applied",
            "Shortlisted",
            "Selected",
            "Rejected"
        ]

        if status not in allowed:
            return False, "Invalid Status."

        application.status = status

        db.session.commit()

        return True, application

    @staticmethod
    def schedule_interview(application_id, interview_date):

        application = Application.query.get(application_id)

        if application is None:
            return False, "Application not found."

        application.interview_date = interview_date
        application.status = "Shortlisted"

        db.session.commit()

        return True, application

    @staticmethod
    def delete(application_id):

        application = Application.query.get(application_id)

        if application is None:
            return False, "Application not found."

        db.session.delete(application)
        db.session.commit()

        return True, "Application deleted successfully."

    @staticmethod
    def get_by_id(application_id):

        return Application.query.get(application_id)

    @staticmethod
    def total_applications():

        return Application.query.count()

    @staticmethod
    def selected_students():

        return Application.query.filter_by(
            status="Selected"
        ).count()

    @staticmethod
    def shortlisted_students():

        return Application.query.filter_by(
            status="Shortlisted"
        ).count()

    @staticmethod
    def rejected_students():

        return Application.query.filter_by(
            status="Rejected"
        ).count()