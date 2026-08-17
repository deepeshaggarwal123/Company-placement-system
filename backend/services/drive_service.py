# backend/services/drive_service.py

from datetime import date

from extensions import db
from models.drive import PlacementDrive


class DriveService:

    # ==========================================
    # Create Placement Drive
    # ==========================================

    @staticmethod
    def create(data):

        drive = PlacementDrive(

            company_id=data["company_id"],

            job_title=data["job_title"],

            job_description=data["job_description"],

            eligible_branch=data["eligible_branch"],

            eligible_year=data["eligible_year"],

            minimum_cgpa=data["minimum_cgpa"],

            application_deadline=data["application_deadline"],

            status="Pending",

            is_active=True

        )

        db.session.add(drive)
        db.session.commit()

        return drive

    # ==========================================
    # Get All Drives
    # ==========================================

    @staticmethod
    def get_all():

        return PlacementDrive.query.all()

    # ==========================================
    # Get Approved Drives
    # ==========================================

    @staticmethod
    def get_approved():

        return PlacementDrive.query.filter_by(
            status="Approved",
            is_active=True
        ).all()

    # ==========================================
    # Get Drive By ID
    # ==========================================

    @staticmethod
    def get(drive_id):

        return PlacementDrive.query.get(drive_id)

    # ==========================================
    # Company Drives
    # ==========================================

    @staticmethod
    def company_drives(company_id):

        return PlacementDrive.query.filter_by(
            company_id=company_id
        ).all()

    # ==========================================
    # Eligible Drives
    # ==========================================

    @staticmethod
    def eligible_drives(student):

        return PlacementDrive.query.filter(

            PlacementDrive.status == "Approved",

            PlacementDrive.is_active == True,

            PlacementDrive.eligible_branch == student.branch,

            PlacementDrive.eligible_year == student.year,

            PlacementDrive.minimum_cgpa <= student.cgpa,

            PlacementDrive.application_deadline >= date.today()

        ).all()

    # ==========================================
    # Search Drives
    # ==========================================

    @staticmethod
    def search(keyword):

        return PlacementDrive.query.filter(

            PlacementDrive.job_title.ilike(
                f"%{keyword}%"
            )

        ).all()

    # ==========================================
    # Update Drive
    # ==========================================

    @staticmethod
    def update(drive_id, data):

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Drive not found."

        drive.job_title = data.get(
            "job_title",
            drive.job_title
        )

        drive.job_description = data.get(
            "job_description",
            drive.job_description
        )

        drive.eligible_branch = data.get(
            "eligible_branch",
            drive.eligible_branch
        )

        drive.eligible_year = data.get(
            "eligible_year",
            drive.eligible_year
        )

        drive.minimum_cgpa = data.get(
            "minimum_cgpa",
            drive.minimum_cgpa
        )

        drive.application_deadline = data.get(
            "application_deadline",
            drive.application_deadline
        )

        db.session.commit()

        return True, drive

    # ==========================================
    # Approve Drive
    # ==========================================

    @staticmethod
    def approve(drive_id):

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Drive not found."

        drive.status = "Approved"

        db.session.commit()

        return True, drive

    # ==========================================
    # Reject Drive
    # ==========================================

    @staticmethod
    def reject(drive_id):

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Drive not found."

        drive.status = "Rejected"

        db.session.commit()

        return True, drive

    # ==========================================
    # Close Drive
    # ==========================================

    @staticmethod
    def close(drive_id):

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Drive not found."

        drive.status = "Closed"
        drive.is_active = False

        db.session.commit()

        return True, drive

    # ==========================================
    # Reopen Drive
    # ==========================================

    @staticmethod
    def reopen(drive_id):

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Drive not found."

        drive.status = "Approved"
        drive.is_active = True

        db.session.commit()

        return True, drive

    # ==========================================
    # Delete Drive
    # ==========================================

    @staticmethod
    def delete(drive_id):

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Drive not found."

        db.session.delete(drive)
        db.session.commit()

        return True, "Drive deleted successfully."

    # ==========================================
    # Dashboard Statistics
    # ==========================================

    @staticmethod
    def total():

        return PlacementDrive.query.count()

    @staticmethod
    def approved():

        return PlacementDrive.query.filter_by(
            status="Approved"
        ).count()

    @staticmethod
    def pending():

        return PlacementDrive.query.filter_by(
            status="Pending"
        ).count()

    @staticmethod
    def rejected():

        return PlacementDrive.query.filter_by(
            status="Rejected"
        ).count()

    @staticmethod
    def closed():

        return PlacementDrive.query.filter_by(
            status="Closed"
        ).count()