# backend/tasks.py

import csv
import os
from datetime import datetime, timedelta

from celery_worker import celery
from flask import current_app
from flask_mail import Message

from extensions import db, mail
from models.student import Student
from models.company import Company
from models.drive import PlacementDrive
from models.application import Application


# ============================================================
# DAILY REMINDER
# ============================================================

@celery.task(name="tasks.daily_reminder")
def daily_reminder():

    today = datetime.utcnow().date()
    upcoming = today + timedelta(days=2)

    drives = PlacementDrive.query.filter(
        PlacementDrive.application_deadline >= today,
        PlacementDrive.application_deadline <= upcoming,
        PlacementDrive.status == "Approved"
    ).all()

    if not drives:
        return "No upcoming drives."

    students = Student.query.all()

    for student in students:

        if not student.email:
            continue

        body = "Upcoming Placement Drives\n\n"

        for drive in drives:
            body += (
                f"Company : {drive.company.company_name}\n"
                f"Job : {drive.job_title}\n"
                f"Deadline : {drive.application_deadline}\n\n"
            )

        try:
            msg = Message(
                subject="Placement Drive Reminder",
                recipients=[student.email],
                body=body
            )

            mail.send(msg)

        except Exception as e:
            print(e)

    return "Daily Reminder Sent"


# ============================================================
# MONTHLY REPORT
# ============================================================

@celery.task(name="tasks.monthly_report")
def monthly_report():
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    import tempfile

    total_students = Student.query.count()
    total_companies = Company.query.count()
    total_drives = PlacementDrive.query.count()
    total_applications = Application.query.count()
    selected = Application.query.filter_by(status="Selected").count()

    admin_email = current_app.config.get("MAIL_USERNAME", "admin@placement.com")

    # Generate PDF
    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, f"monthly_report_{datetime.now().strftime('%Y%m')}.pdf")
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 750, "Placement Portal Monthly Report")
    
    c.setFont("Helvetica", 14)
    c.drawString(50, 700, f"Total Students: {total_students}")
    c.drawString(50, 670, f"Total Companies: {total_companies}")
    c.drawString(50, 640, f"Placement Drives: {total_drives}")
    c.drawString(50, 610, f"Total Applications: {total_applications}")
    c.drawString(50, 580, f"Selected Students: {selected}")
    
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 530, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.save()

    try:
        msg = Message(
            subject="Monthly Placement Report",
            recipients=[admin_email],
            body="Please find the monthly placement report attached."
        )
        with current_app.open_resource(pdf_path) as fp:
            msg.attach("monthly_report.pdf", "application/pdf", fp.read())

        mail.send(msg)
        return "Monthly Report PDF Sent"
    except Exception as e:
        return str(e)
    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)


# ============================================================
# CSV EXPORT
# ============================================================

@celery.task(name="tasks.export_student_csv")
def export_student_csv(student_id):

    student = Student.query.get(student_id)

    if student is None:
        return "Student not found."

    applications = Application.query.filter_by(
        student_id=student.id
    ).all()

    export_folder = current_app.config["EXPORT_FOLDER"]

    os.makedirs(export_folder, exist_ok=True)

    filename = os.path.join(
        export_folder,
        f"student_{student.id}.csv"
    )

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student ID",
            "Student Name",
            "Company",
            "Drive",
            "Status",
            "Applied Date"
        ])

        for application in applications:

            writer.writerow([
                student.id,
                student.name,
                application.drive.company.company_name,
                application.drive.job_title,
                application.status,
                application.application_date
            ])

    return filename


# ============================================================
# SEND INTERVIEW MAIL
# ============================================================

@celery.task(name="tasks.send_interview_mail")
def send_interview_mail(
        email,
        company,
        job,
        interview_date
):

    body = f"""
Congratulations!

You have been shortlisted.

Company :
{company}

Job :
{job}

Interview Date :
{interview_date}

Best of Luck.
"""

    try:

        msg = Message(
            subject="Interview Scheduled",
            recipients=[email],
            body=body
        )

        mail.send(msg)

        return "Interview Mail Sent"

    except Exception as e:
        return str(e)


# ============================================================
# CACHE CLEANUP
# ============================================================

@celery.task(name="tasks.clear_cache")
def clear_cache():

    from extensions import cache

    cache.clear()

    return "Redis Cache Cleared"