# backend/routes/student.py

import os
from flask import Blueprint, jsonify, request, send_file, current_app
from flask_security import auth_required, current_user
from werkzeug.utils import secure_filename

from extensions import db
from models.student import Student
from models.drive import PlacementDrive
from models.application import Application
from services.student_service import StudentService
from services.application_service import ApplicationService
from services.export_service import ExportService

student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/api/student"
)


# ==========================================================
# Student Dashboard
# ==========================================================

@student_bp.route("/dashboard", methods=["GET"])
@auth_required("session")
def dashboard():

    student = Student.query.filter_by(
        user_id=current_user.id
    ).first()

    if student is None:
        return jsonify({
            "message": "Student profile not found."
        }), 404

    total_applications = Application.query.filter_by(
        student_id=student.id
    ).count()

    shortlisted = Application.query.filter_by(
        student_id=student.id,
        status="Shortlisted"
    ).count()

    selected = Application.query.filter_by(
        student_id=student.id,
        status="Selected"
    ).count()

    approved_drives = PlacementDrive.query.filter_by(
        status="Approved",
        is_active=True
    ).count()

    # Get available eligible drives (student not yet applied, eligible requirements match)
    applied_drive_ids = [app.drive_id for app in Application.query.filter_by(student_id=student.id).all()]
    eligible_drives = PlacementDrive.query.filter(
        PlacementDrive.status == "Approved",
        PlacementDrive.is_active == True,
        PlacementDrive.eligible_branch == student.branch,
        PlacementDrive.eligible_year == student.year,
        PlacementDrive.minimum_cgpa <= student.cgpa,
        ~PlacementDrive.id.in_(applied_drive_ids) if applied_drive_ids else True
    ).all()

    # Get recent applications
    applications_list = Application.query.filter_by(student_id=student.id).all()

    return jsonify({
        "stats": {
            "available_drives": len(eligible_drives),
            "applied_drives": total_applications,
            "shortlisted": shortlisted,
            "selected": selected
        },
        "student": {
            "name": student.full_name,
            "branch": student.branch,
            "cgpa": student.cgpa
        },
        "drives": [
            {
                "id": drive.id,
                "company_name": drive.company.company_name if drive.company else "Unknown",
                "job_title": drive.job_title,
                "package": drive.package or 0
            }
            for drive in eligible_drives
        ],
        "applications": [
            {
                "id": app.id,
                "company_name": app.drive.company.company_name if app.drive and app.drive.company else "Unknown",
                "job_title": app.drive.job_title if app.drive else "Unknown",
                "status": app.status
            }
            for app in applications_list
        ]
    })


# ==========================================================
# Student Profile
# ==========================================================

@student_bp.route("/profile", methods=["GET"])
@auth_required("session")
def profile():

    student = Student.query.filter_by(
        user_id=current_user.id
    ).first()

    if student is None:
        return jsonify({
            "message": "Student not found."
        }), 404

    return jsonify(student.to_dict())


# ==========================================================
# Update Student Profile
# ==========================================================

@student_bp.route("/profile", methods=["PUT"])
@auth_required("session")
def update_profile():

    student = Student.query.filter_by(
        user_id=current_user.id
    ).first()

    if student is None:
        return jsonify({
            "message": "Student not found."
        }), 404

    data = request.get_json()
    success, res = StudentService.update_profile(current_user.id, data)
    if not success:
        return jsonify({"message": res}), 400

    return jsonify({
        "message": "Profile updated successfully.",
        "student": res.to_dict()
    })


# ==========================================================
# Available Drives
# ==========================================================

@student_bp.route("/drives", methods=["GET"])
@auth_required("session")
def drives():
    student = Student.query.filter_by(user_id=current_user.id).first()
    if student is None:
        return jsonify({"message": "Student profile not found."}), 404

    drives_list = StudentService.eligible_drives(current_user.id)
    formatted = []
    # Check if student applied to any drive
    applied_drives = {app.drive_id: app.status for app in Application.query.filter_by(student_id=student.id).all()}
    for d in drives_list:
        item = d.to_dict()
        item["company_name"] = d.company.company_name if d.company else "Unknown"
        item["min_cgpa"] = d.minimum_cgpa
        item["location"] = d.job_location
        item["deadline"] = d.application_deadline.strftime("%Y-%m-%d") if d.application_deadline else None
        item["branch"] = d.eligible_branch
        item["applied"] = d.id in applied_drives
        formatted.append(item)

    return jsonify({
        "drives": formatted,
        "student": student.to_dict()
    })


# ==========================================================
# Search Drives
# ==========================================================

@student_bp.route("/drives/search", methods=["GET"])
@auth_required("session")
def search_drives():
    keyword = request.args.get("query", "")
    student = Student.query.filter_by(user_id=current_user.id).first()
    if student is None:
        return jsonify({"message": "Student not found."}), 404

    drives_list = StudentService.eligible_drives(current_user.id)
    applied_drives = {app.drive_id: app.status for app in Application.query.filter_by(student_id=student.id).all()}
    formatted = []
    for d in drives_list:
        if keyword.lower() in d.job_title.lower() or (d.company and keyword.lower() in d.company.company_name.lower()):
            item = d.to_dict()
            item["company_name"] = d.company.company_name if d.company else "Unknown"
            item["min_cgpa"] = d.minimum_cgpa
            item["location"] = d.job_location
            item["deadline"] = d.application_deadline.strftime("%Y-%m-%d") if d.application_deadline else None
            item["branch"] = d.eligible_branch
            item["applied"] = d.id in applied_drives
            formatted.append(item)

    return jsonify({
        "drives": formatted,
        "student": student.to_dict()
    })


# ==========================================================
# Drive Details
# ==========================================================

@student_bp.route("/drives/<int:drive_id>", methods=["GET"])
@auth_required("session")
def get_drive(drive_id):
    drive = PlacementDrive.query.get_or_404(drive_id)
    return jsonify(drive.to_dict())


# ==========================================================
# Apply For Drive
# ==========================================================

@student_bp.route("/apply/<int:drive_id>", methods=["POST"])
@auth_required("session")
def apply_drive(drive_id):
    success, res = ApplicationService.apply(current_user.id, drive_id)
    if not success:
        return jsonify({"message": res}), 400
    return jsonify({"message": "Applied successfully."}), 201


# ==========================================================
# Applications
# ==========================================================

@student_bp.route("/applications", methods=["GET"])
@auth_required("session")
def applications():
    student = Student.query.filter_by(user_id=current_user.id).first()
    if student is None:
        return jsonify({"message": "Student profile not found."}), 404

    apps = Application.query.filter_by(student_id=student.id).all()
    data = []
    for app in apps:
        data.append({
            "id": app.id,
            "company_name": app.drive.company.company_name if app.drive and app.drive.company else "Unknown",
            "job_title": app.drive.job_title if app.drive else "Unknown",
            "status": app.status,
            "application_date": app.application_date.strftime("%Y-%m-%d") if app.application_date else None,
            "interview_date": app.interview_date.strftime("%Y-%m-%d") if app.interview_date else None
        })
    return jsonify(data)


# ==========================================================
# Application Status
# ==========================================================

@student_bp.route("/application/<int:application_id>", methods=["GET"])
@auth_required("session")
def application_status(application_id):
    app = Application.query.get_or_404(application_id)
    return jsonify({
        "id": app.id,
        "status": app.status,
        "company_name": app.drive.company.company_name if app.drive and app.drive.company else "Unknown",
        "job_title": app.drive.job_title if app.drive else "Unknown"
    })


# ==========================================================
# Resume Upload
# ==========================================================

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

@student_bp.route("/upload-resume", methods=["POST"])
@auth_required("session")
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"message": "No file uploaded."}), 400
    file = request.files["resume"]
    if file.filename == "":
        return jsonify({"message": "Empty filename."}), 400

    if file and allowed_file(file.filename):
        student = Student.query.filter_by(user_id=current_user.id).first()
        if not student:
            return jsonify({"message": "Student not found."}), 404

        ext = file.filename.rsplit(".", 1)[1].lower()
        # Make a safe clean name
        filename = f"resume_{student.id}.{ext}"
        
        upload_dir = current_app.config["UPLOAD_FOLDER"]
        os.makedirs(upload_dir, exist_ok=True)
        filepath = os.path.join(upload_dir, filename)
        file.save(filepath)

        StudentService.upload_resume(current_user.id, filename)
        return jsonify({"message": "Resume uploaded successfully.", "filename": filename})
    
    return jsonify({"message": "Invalid file type."}), 400


# ==========================================================
# Retrieve Resume
# ==========================================================

@student_bp.route("/resume", methods=["GET"])
@auth_required("session")
def get_resume():
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student or not student.resume:
        return jsonify({"message": "Resume not found."}), 404

    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], student.resume)
    if os.path.exists(filepath):
        return send_file(filepath)
    return jsonify({"message": "Resume file missing on server."}), 404


# ==========================================================
# Delete Resume
# ==========================================================

@student_bp.route("/resume", methods=["DELETE"])
@auth_required("session")
def delete_resume():
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student or not student.resume:
        return jsonify({"message": "No resume found to delete."}), 404

    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], student.resume)
    if os.path.exists(filepath):
        os.remove(filepath)
    
    student.resume = None
    db.session.commit()
    return jsonify({"message": "Resume deleted successfully."})


# ==========================================================
# Placement History
# ==========================================================

@student_bp.route("/placement-history", methods=["GET"])
@auth_required("session")
def placement_history():
    history_list = StudentService.placement_history(current_user.id)
    data = []
    for app in history_list:
        data.append({
            "id": app.id,
            "company_name": app.drive.company.company_name if app.drive and app.drive.company else "Unknown",
            "job_title": app.drive.job_title if app.drive else "Unknown",
            "package": app.drive.package or 0,
            "application_date": app.application_date.strftime("%Y-%m-%d") if app.application_date else None,
            "status": app.status
        })
    return jsonify(data)


# ==========================================================
# Export Applications CSV
# ==========================================================

@student_bp.route("/export-applications", methods=["GET"])
@auth_required("session")
def export_applications():
    success, filepath = ExportService.export_student_applications(current_user.id)
    if not success:
        return jsonify({"message": filepath}), 404
    
    return send_file(
        filepath,
        mimetype="text/csv",
        as_attachment=True,
        download_name="applications.csv"
    )