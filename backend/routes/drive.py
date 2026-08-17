# backend/routes/drive.py

from datetime import date
from flask import Blueprint, jsonify, request
from flask_security import auth_required, current_user

from extensions import db
from models.drive import PlacementDrive
from models.student import Student
from models.company import Company
from models.application import Application
from services.drive_service import DriveService
from services.company_service import CompanyService
from services.application_service import ApplicationService

drive_bp = Blueprint(
    "drive",
    __name__,
    url_prefix="/api/drives"
)


# ==========================================================
# Get Approved Drives
# ==========================================================

@drive_bp.route("/", methods=["GET"])
@drive_bp.route("/approved", methods=["GET"])
@auth_required("session")
def get_drives():

    drives = PlacementDrive.query.filter_by(
        status="Approved",
        is_active=True
    ).all()

    return jsonify([drive.to_dict() for drive in drives])


# ==========================================================
# Search Drives
# ==========================================================

@drive_bp.route("/search", methods=["GET"])
@auth_required("session")
def search_drives():

    keyword = request.args.get("query", request.args.get("q", ""))

    drives = PlacementDrive.query.filter(
        PlacementDrive.status == "Approved",
        PlacementDrive.job_title.ilike(f"%{keyword}%")
    ).all()

    return jsonify([drive.to_dict() for drive in drives])


# ==========================================================
# Eligible Drives
# ==========================================================

@drive_bp.route("/eligible", methods=["GET"])
@auth_required("session")
def eligible_drives():

    student = Student.query.filter_by(
        user_id=current_user.id
    ).first()

    if student is None:
        return jsonify({
            "message": "Student not found."
        }), 404

    drives = DriveService.eligible_drives(student)
    return jsonify([drive.to_dict() for drive in drives])


# ==========================================================
# Company Drives
# ==========================================================

@drive_bp.route("/company/<int:company_id>", methods=["GET"])
@auth_required("session")
def company_drives(company_id):

    company = Company.query.get_or_404(company_id)

    drives = PlacementDrive.query.filter_by(
        company_id=company.id
    ).all()

    return jsonify([drive.to_dict() for drive in drives])


# ==========================================================
# Create, Read, Update, Delete Drive
# ==========================================================

@drive_bp.route("/<int:drive_id>", methods=["GET"])
@auth_required("session")
def get_drive(drive_id):
    drive = PlacementDrive.query.get_or_404(drive_id)
    return jsonify(drive.to_dict())


@drive_bp.route("/create", methods=["POST"])
@auth_required("session")
def create_drive():
    data = request.get_json()
    from datetime import datetime
    try:
        if "application_deadline" in data:
            data["application_deadline"] = datetime.strptime(data["application_deadline"], "%Y-%m-%d").date()
    except Exception:
        return jsonify({"message": "Invalid deadline format."}), 400

    # Retrieve company by current user ID
    company = Company.query.filter_by(user_id=current_user.id).first()
    if not company:
        return jsonify({"message": "Only approved companies can create drives."}), 403
    data["company_id"] = company.id

    drive = DriveService.create(data)
    return jsonify(drive.to_dict()), 201


@drive_bp.route("/<int:drive_id>", methods=["PUT"])
@auth_required("session")
def update_drive(drive_id):
    data = request.get_json()
    from datetime import datetime
    try:
        if "application_deadline" in data:
            data["application_deadline"] = datetime.strptime(data["application_deadline"], "%Y-%m-%d").date()
    except Exception:
        pass
    success, drive_res = DriveService.update(drive_id, data)
    if not success:
        return jsonify({"message": drive_res}), 400
    return jsonify(drive_res.to_dict())


@drive_bp.route("/<int:drive_id>", methods=["DELETE"])
@auth_required("session")
def delete_drive(drive_id):
    success, msg = DriveService.delete(drive_id)
    if not success:
        return jsonify({"message": msg}), 400
    return jsonify({"message": msg})


# ==========================================================
# Approval, Rejection, Closing
# ==========================================================

@drive_bp.route("/<int:drive_id>/approve", methods=["PUT"])
@auth_required("session")
def approve_drive(drive_id):
    success, drive = DriveService.approve(drive_id)
    if not success:
        return jsonify({"message": drive}), 400
    return jsonify(drive.to_dict())


@drive_bp.route("/<int:drive_id>/reject", methods=["PUT"])
@auth_required("session")
def reject_drive(drive_id):
    success, drive = DriveService.reject(drive_id)
    if not success:
        return jsonify({"message": drive}), 400
    return jsonify(drive.to_dict())


@drive_bp.route("/<int:drive_id>/close", methods=["PUT"])
@auth_required("session")
def close_drive(drive_id):
    success, drive = DriveService.close(drive_id)
    if not success:
        return jsonify({"message": drive}), 400
    return jsonify(drive.to_dict())


# ==========================================================
# Student Actions (Apply & Status)
# ==========================================================

@drive_bp.route("/<int:drive_id>/apply", methods=["POST"])
@auth_required("session")
def student_apply(drive_id):
    success, res = ApplicationService.apply(current_user.id, drive_id)
    if not success:
        return jsonify({"message": res}), 400
    return jsonify({"message": "Applied successfully.", "application": res.to_dict()}), 201


@drive_bp.route("/<int:drive_id>/application-status", methods=["GET"])
@auth_required("session")
def get_drive_application_status(drive_id):
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student:
        return jsonify({"message": "Student not found."}), 404
    app = Application.query.filter_by(student_id=student.id, drive_id=drive_id).first()
    if not app:
        return jsonify({"applied": False, "status": None})
    return jsonify({"applied": True, "status": app.status, "application_id": app.id})


@drive_bp.route("/<int:drive_id>/applications", methods=["GET"])
@auth_required("session")
def get_drive_applications(drive_id):
    apps = ApplicationService.get_drive_applications(drive_id)
    data = []
    for app in apps:
        data.append({
            "id": app.id,
            "student_name": app.student.full_name if app.student else "Unknown",
            "email": app.student.email if app.student else "Unknown",
            "cgpa": app.student.cgpa if app.student else 0.0,
            "branch": app.student.branch if app.student else "Unknown",
            "status": app.status
        })
    return jsonify(data)