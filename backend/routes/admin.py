# backend/routes/admin.py

import os
import csv
from datetime import datetime
from flask import Blueprint, jsonify, request, send_file, current_app
from flask_security import auth_required, roles_required

from extensions import db
from models.student import Student
from models.company import Company
from models.drive import PlacementDrive
from models.application import Application
from services.student_service import StudentService
from services.company_service import CompanyService
from services.drive_service import DriveService
from services.report_service import ReportService

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")


# ==========================================================
# Admin Dashboard
# ==========================================================
@admin_bp.route("/dashboard", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def dashboard():

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

    selected_students = Application.query.filter_by(
        status="Selected"
    ).count()

    recent_drives = PlacementDrive.query.order_by(PlacementDrive.created_at.desc()).limit(5).all()
    recent_applications = Application.query.order_by(Application.application_date.desc()).limit(5).all()

    return jsonify({
        "stats": {
            "students": total_students,
            "companies": total_companies,
            "drives": total_drives,
            "applications": total_applications,
            "approved_companies": approved_companies,
            "pending_companies": pending_companies,
            "approved_drives": approved_drives,
            "pending_drives": pending_drives,
            "selected_students": selected_students
        },
        "drives": [d.to_dict() for d in recent_drives],
        "applications": [
            {
                "id": app.id,
                "student_name": app.student.full_name if app.student else "Unknown",
                "company_name": app.drive.company.company_name if app.drive and app.drive.company else "Unknown",
                "status": app.status
            }
            for app in recent_applications
        ]
    })


# ==========================================================
# Get All Students & Search
# ==========================================================
@admin_bp.route("/students", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])


@admin_bp.route("/students/search", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def search_students():
    keyword = request.args.get("query", "")
    students = StudentService.search(keyword)
    return jsonify([student.to_dict() for student in students])


# ==========================================================
# Student Actions (Deactivate, Blacklist)
# ==========================================================
@admin_bp.route("/student/<int:student_id>/deactivate", methods=["PUT"])
@auth_required("session")
@roles_required("admin")
def deactivate_student(student_id):
    student = Student.query.get_or_404(student_id)
    # Deactivate associated User account
    from models.user import User
    user = User.query.get(student.user_id)
    if user:
        user.active = False
    student.is_active = False
    db.session.commit()
    return jsonify({"message": "Student deactivated successfully."})


@admin_bp.route("/student/<int:student_id>/blacklist", methods=["PUT"])
@auth_required("session")
@roles_required("admin")
def blacklist_student(student_id):
    success, student_res = StudentService.blacklist(student_id)
    if not success:
        return jsonify({"message": student_res}), 400
    return jsonify({"message": "Student blacklisted successfully."})


# ==========================================================
# Get All Companies & Search
# ==========================================================
@admin_bp.route("/companies", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def get_companies():
    companies = Company.query.all()
    return jsonify([company.to_dict() for company in companies])


@admin_bp.route("/companies/search", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def search_companies():
    keyword = request.args.get("query", "")
    companies = Company.query.filter(Company.company_name.ilike(f"%{keyword}%")).all()
    return jsonify([company.to_dict() for company in companies])


# ==========================================================
# Company Actions (Approve, Reject, Blacklist)
# ==========================================================
@admin_bp.route("/company/<int:company_id>/approve", methods=["PUT"])
@auth_required("session")
@roles_required("admin")
def approve_company(company_id):
    company = Company.query.get_or_404(company_id)
    company.approval_status = "Approved"
    db.session.commit()
    return jsonify({"message": "Company approved successfully."})


@admin_bp.route("/company/<int:company_id>/reject", methods=["PUT"])
@auth_required("session")
@roles_required("admin")
def reject_company(company_id):
    company = Company.query.get_or_404(company_id)
    company.approval_status = "Rejected"
    db.session.commit()
    return jsonify({"message": "Company request rejected successfully."})


@admin_bp.route("/company/<int:company_id>/blacklist", methods=["PUT"])
@auth_required("session")
@roles_required("admin")
def blacklist_company(company_id):
    company = Company.query.get_or_404(company_id)
    company.approval_status = "Blacklisted"
    db.session.commit()
    return jsonify({"message": "Company blacklisted successfully."})


# ==========================================================
# Get All Placement Drives & Actions
# ==========================================================
@admin_bp.route("/drives", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def get_drives():
    drives = PlacementDrive.query.all()
    return jsonify([drive.to_dict() for drive in drives])


@admin_bp.route("/drive/<int:drive_id>/approve", methods=["PUT"])
@auth_required("session")
@roles_required("admin")
def approve_drive(drive_id):
    success, drive_res = DriveService.approve(drive_id)
    if not success:
        return jsonify({"message": drive_res}), 400
    return jsonify({"message": "Placement drive approved successfully."})


@admin_bp.route("/drive/<int:drive_id>/reject", methods=["PUT"])
@auth_required("session")
@roles_required("admin")
def reject_drive(drive_id):
    success, drive_res = DriveService.reject(drive_id)
    if not success:
        return jsonify({"message": drive_res}), 400
    return jsonify({"message": "Placement drive rejected successfully."})


# ==========================================================
# Get All Applications
# ==========================================================
@admin_bp.route("/applications", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def get_applications():

    applications = Application.query.all()

    data = []

    for application in applications:

        data.append({

            "application_id": application.id,

            "student": application.student.full_name if application.student else "Unknown",

            "company": application.drive.company.company_name if application.drive and application.drive.company else "Unknown",

            "job_title": application.drive.job_title if application.drive else "Unknown",

            "status": application.status,

            "application_date": application.application_date.strftime("%Y-%m-%d") if application.application_date else None

        })

    return jsonify(data)


# ==========================================================
# Reports
# ==========================================================

@admin_bp.route("/reports/monthly", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def get_placement_report():
    report = ReportService.monthly_report()
    return jsonify(report)


@admin_bp.route("/reports/export", methods=["GET"])
@auth_required("session")
@roles_required("admin")
def export_report():
    report = ReportService.monthly_report()
    
    # Generate CSV response manually
    export_folder = os.path.join(current_app.root_path, "exports")
    os.makedirs(export_folder, exist_ok=True)
    filename = f"monthly_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = os.path.join(export_folder, filename)
    
    with open(filepath, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Metric", "Value"])
        for key, val in report.items():
            writer.writerow([key.replace("_", " ").title(), val])
            
    return send_file(
        filepath,
        mimetype="text/csv",
        as_attachment=True,
        download_name="monthly_placement_report.csv"
    )