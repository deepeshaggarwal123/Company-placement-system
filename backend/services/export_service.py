# backend/services/export_service.py

import csv
import os
from datetime import datetime

from flask import current_app

from models.student import Student
from models.application import Application


class ExportService:

    # =====================================================
    # Export Student Applications as CSV
    # =====================================================

    @staticmethod
    def export_student_applications(student_user_id):

        student = Student.query.filter_by(
            user_id=student_user_id
        ).first()

        if student is None:
            return False, "Student not found."

        applications = Application.query.filter_by(
            student_id=student.id
        ).all()

        export_folder = os.path.join(
            current_app.root_path,
            "exports"
        )

        os.makedirs(export_folder, exist_ok=True)

        filename = (
            f"applications_"
            f"{student.id}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        filepath = os.path.join(
            export_folder,
            filename
        )

        with open(
            filepath,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow([
                "Application ID",
                "Student ID",
                "Student Name",
                "Company",
                "Job Title",
                "Application Date",
                "Status",
                "Interview Date"
            ])

            for application in applications:

                writer.writerow([

                    application.id,

                    student.id,

                    student.full_name,

                    application.drive.company.company_name,

                    application.drive.job_title,

                    application.application_date,

                    application.status,

                    application.interview_date

                ])

        return True, filepath

    # =====================================================
    # Export Drive Applicants
    # =====================================================

    @staticmethod
    def export_drive_applicants(drive):

        export_folder = os.path.join(
            current_app.root_path,
            "exports"
        )

        os.makedirs(export_folder, exist_ok=True)

        filename = (
            f"drive_{drive.id}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        filepath = os.path.join(
            export_folder,
            filename
        )

        with open(
            filepath,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student Name",
                "Email",
                "Branch",
                "CGPA",
                "Status"
            ])

            for application in drive.applications:

                student = application.student

                writer.writerow([

                    student.full_name,

                    student.email,

                    student.branch,

                    student.cgpa,

                    application.status

                ])

        return filepath

    # =====================================================
    # Delete Export File
    # =====================================================

    @staticmethod
    def delete_file(filepath):

        if os.path.exists(filepath):

            os.remove(filepath)

            return True

        return False