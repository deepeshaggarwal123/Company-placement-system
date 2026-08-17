# backend/utils/csv_export.py

import csv
import os
from datetime import datetime

from flask import current_app


class CSVExport:

    @staticmethod
    def create_export_folder():
        """
        Create exports directory if it doesn't exist.
        """

        export_dir = os.path.join(
            current_app.root_path,
            "exports"
        )

        os.makedirs(export_dir, exist_ok=True)

        return export_dir

    @staticmethod
    def export_student_history(student, applications):
        """
        Export student's placement history.
        """

        export_dir = CSVExport.create_export_folder()

        filename = (
            f"student_{student.id}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        filepath = os.path.join(
            export_dir,
            filename
        )

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Application ID",
                "Student Name",
                "Company",
                "Job Title",
                "Application Date",
                "Status",
                "Interview Date"
            ])

            for app in applications:

                writer.writerow([

                    app.id,

                    student.full_name,

                    app.drive.company.company_name,

                    app.drive.job_title,

                    app.application_date,

                    app.status,

                    app.interview_date

                ])

        return filepath

    @staticmethod
    def export_drive_applicants(drive):
        """
        Export all applicants of one placement drive.
        """

        export_dir = CSVExport.create_export_folder()

        filename = (
            f"drive_{drive.id}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        filepath = os.path.join(
            export_dir,
            filename
        )

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student",
                "Enrollment",
                "Branch",
                "CGPA",
                "Email",
                "Phone",
                "Status"
            ])

            for application in drive.applications:

                student = application.student

                writer.writerow([

                    student.full_name,

                    student.enrollment_no,

                    student.branch,

                    student.cgpa,

                    student.email,

                    student.phone,

                    application.status

                ])

        return filepath

    @staticmethod
    def delete_file(filepath):
        """
        Delete exported CSV file.
        """

        if os.path.exists(filepath):

            os.remove(filepath)

            return True

        return False