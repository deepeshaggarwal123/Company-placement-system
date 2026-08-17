# backend/services/company_service.py

from datetime import datetime

from extensions import db
from models.company import Company
from models.drive import PlacementDrive
from models.application import Application


class CompanyService:

    # =====================================================
    # Dashboard
    # =====================================================

    @staticmethod
    def dashboard(user_id):

        company = Company.query.filter_by(
            user_id=user_id
        ).first()

        if company is None:
            return None

        total_drives = PlacementDrive.query.filter_by(
            company_id=company.id
        ).count()

        approved_drives = PlacementDrive.query.filter_by(
            company_id=company.id,
            status="Approved"
        ).count()

        pending_drives = PlacementDrive.query.filter_by(
            company_id=company.id,
            status="Pending"
        ).count()

        total_applications = 0

        drives = PlacementDrive.query.filter_by(
            company_id=company.id
        ).all()

        for drive in drives:
            total_applications += Application.query.filter_by(
                drive_id=drive.id
            ).count()

        return {

            "company_name": company.company_name,

            "approval_status": company.approval_status,

            "total_drives": total_drives,

            "approved_drives": approved_drives,

            "pending_drives": pending_drives,

            "applications": total_applications

        }

    # =====================================================
    # Get Profile
    # =====================================================

    @staticmethod
    def get_profile(user_id):

        return Company.query.filter_by(
            user_id=user_id
        ).first()

    # =====================================================
    # Update Profile
    # =====================================================

    @staticmethod
    def update_profile(user_id, data):

        company = Company.query.filter_by(
            user_id=user_id
        ).first()

        if company is None:
            return False, "Company not found."

        company.company_name = data.get(
            "company_name",
            company.company_name
        )

        company.website = data.get(
            "website",
            company.website
        )

        company.hr_name = data.get(
            "hr_name",
            company.hr_name
        )

        company.hr_email = data.get(
            "hr_email",
            company.hr_email
        )

        company.hr_phone = data.get(
            "hr_phone",
            company.hr_phone
        )

        company.address = data.get(
            "address",
            company.address
        )

        company.description = data.get(
            "description",
            company.description
        )

        company.industry = data.get(
            "industry",
            company.industry
        )

        db.session.commit()

        return True, company

    # =====================================================
    # Create Drive
    # =====================================================

    @staticmethod
    def create_drive(user_id, data):

        company = Company.query.filter_by(
            user_id=user_id
        ).first()

        if company is None:
            return False, "Company not found."

        if company.approval_status != "Approved":
            return False, "Company not approved."

        drive = PlacementDrive(
            company_id=company.id,
            job_title=data.get("job_title"),
            job_description=data.get("job_description"),
            job_location=data.get("job_location"),
            package=data.get("package"),
            vacancies=data.get("vacancies", 1),
            eligible_branch=data.get("eligible_branch"),
            eligible_year=data.get("eligible_year"),
            minimum_cgpa=data.get("minimum_cgpa", 0.0),
            application_deadline=data.get("application_deadline"),
            status="Pending",
            is_active=True
        )

        db.session.add(drive)
        db.session.commit()

        return True, drive

    # =====================================================
    # My Drives
    # =====================================================

    @staticmethod
    def my_drives(user_id):

        company = Company.query.filter_by(
            user_id=user_id
        ).first()

        if company is None:
            return []

        return PlacementDrive.query.filter_by(
            company_id=company.id
        ).all()

    # =====================================================
    # Delete Drive
    # =====================================================

    @staticmethod
    def delete_drive(drive_id):

        drive = PlacementDrive.query.get(drive_id)

        if drive is None:
            return False, "Drive not found."

        db.session.delete(drive)
        db.session.commit()

        return True, "Drive deleted."

    # =====================================================
    # Applicants
    # =====================================================

    @staticmethod
    def applicants(drive_id):

        return Application.query.filter_by(
            drive_id=drive_id
        ).all()

    # =====================================================
    # Update Application Status
    # =====================================================

    @staticmethod
    def update_status(application_id, status):

        application = Application.query.get(
            application_id
        )

        if application is None:
            return False, "Application not found."

        application.status = status

        db.session.commit()

        return True, application

    # =====================================================
    # Schedule Interview
    # =====================================================

    @staticmethod
    def schedule_interview(
            application_id,
            interview_date
    ):

        application = Application.query.get(
            application_id
        )

        if application is None:
            return False, "Application not found."

        application.interview_date = interview_date

        application.status = "Shortlisted"

        db.session.commit()

        return True, application

    # =====================================================
    # Total Companies
    # =====================================================

    @staticmethod
    def total_companies():

        return Company.query.count()

    # =====================================================
    # Pending Companies
    # =====================================================

    @staticmethod
    def pending_companies():

        return Company.query.filter_by(
            approval_status="Pending"
        ).count()

    # =====================================================
    # Approved Companies
    # =====================================================

    @staticmethod
    def approved_companies():

        return Company.query.filter_by(
            approval_status="Approved"
        ).count()

    # =====================================================
    # Get Company By ID
    # =====================================================

    @staticmethod
    def get(company_id):

        return Company.query.get(company_id)