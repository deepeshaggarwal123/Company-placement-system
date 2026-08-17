# backend/services/report_service.py

from datetime import datetime

from models.student import Student
from models.company import Company
from models.drive import PlacementDrive
from models.application import Application


class ReportService:

    # =====================================================
    # Monthly Report Data
    # =====================================================

    @staticmethod
    def monthly_report():

        total_students = Student.query.count()

        total_companies = Company.query.count()

        total_drives = PlacementDrive.query.count()

        total_applications = Application.query.count()

        approved_companies = Company.query.filter_by(
            approval_status="Approved"
        ).count()

        pending_companies = Company.query.filter_by(
            approval_status="Pending"
        ).count()

        approved_drives = PlacementDrive.query.filter_by(
            status="Approved"
        ).count()

        pending_drives = PlacementDrive.query.filter_by(
            status="Pending"
        ).count()

        closed_drives = PlacementDrive.query.filter_by(
            status="Closed"
        ).count()

        selected_students = Application.query.filter_by(
            status="Selected"
        ).count()

        shortlisted_students = Application.query.filter_by(
            status="Shortlisted"
        ).count()

        rejected_students = Application.query.filter_by(
            status="Rejected"
        ).count()

        applied_students = Application.query.filter_by(
            status="Applied"
        ).count()

        return {

            "generated_on":
                datetime.now().strftime("%d-%m-%Y %H:%M"),

            "total_students":
                total_students,

            "total_companies":
                total_companies,

            "total_drives":
                total_drives,

            "total_applications":
                total_applications,

            "approved_companies":
                approved_companies,

            "pending_companies":
                pending_companies,

            "approved_drives":
                approved_drives,

            "pending_drives":
                pending_drives,

            "closed_drives":
                closed_drives,

            "selected_students":
                selected_students,

            "shortlisted_students":
                shortlisted_students,

            "rejected_students":
                rejected_students,

            "applied_students":
                applied_students

        }

    # =====================================================
    # Admin Dashboard Report
    # =====================================================

    @staticmethod
    def dashboard():

        return ReportService.monthly_report()

    # =====================================================
    # Company Wise Report
    # =====================================================

    @staticmethod
    def company_report():

        companies = Company.query.all()

        report = []

        for company in companies:

            drives = PlacementDrive.query.filter_by(
                company_id=company.id
            ).all()

            applications = 0
            selected = 0

            for drive in drives:

                apps = Application.query.filter_by(
                    drive_id=drive.id
                ).all()

                applications += len(apps)

                selected += len([
                    a for a in apps
                    if a.status == "Selected"
                ])

            report.append({

                "company_id": company.id,

                "company_name": company.company_name,

                "approval_status": company.approval_status,

                "total_drives": len(drives),

                "applications": applications,

                "selected": selected

            })

        return report

    # =====================================================
    # Student Wise Report
    # =====================================================

    @staticmethod
    def student_report():

        students = Student.query.all()

        report = []

        for student in students:

            applications = Application.query.filter_by(
                student_id=student.id
            ).all()

            report.append({

                "student_id": student.id,

                "name": student.full_name,

                "branch": student.branch,

                "cgpa": student.cgpa,

                "applications": len(applications),

                "selected": len([
                    a for a in applications
                    if a.status == "Selected"
                ]),

                "shortlisted": len([
                    a for a in applications
                    if a.status == "Shortlisted"
                ])

            })

        return report

    # =====================================================
    # Drive Wise Report
    # =====================================================

    @staticmethod
    def drive_report():

        drives = PlacementDrive.query.all()

        report = []

        for drive in drives:

            applications = Application.query.filter_by(
                drive_id=drive.id
            ).all()

            report.append({

                "drive_id": drive.id,

                "company": drive.company.company_name,

                "job_title": drive.job_title,

                "status": drive.status,

                "deadline": drive.application_deadline,

                "applications": len(applications),

                "selected": len([
                    a for a in applications
                    if a.status == "Selected"
                ])

            })

        return report

    # =====================================================
    # Placement Statistics
    # =====================================================

    @staticmethod
    def statistics():

        total = Application.query.count()

        selected = Application.query.filter_by(
            status="Selected"
        ).count()

        rejected = Application.query.filter_by(
            status="Rejected"
        ).count()

        shortlisted = Application.query.filter_by(
            status="Shortlisted"
        ).count()

        applied = Application.query.filter_by(
            status="Applied"
        ).count()

        placement_percentage = 0

        if total > 0:

            placement_percentage = round(
                (selected / total) * 100,
                2
            )

        return {

            "applications": total,

            "selected": selected,

            "shortlisted": shortlisted,

            "rejected": rejected,

            "applied": applied,

            "placement_percentage":
                placement_percentage

        }