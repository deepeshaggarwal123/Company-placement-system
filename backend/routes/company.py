# backend/routes/company.py

from flask import Blueprint, jsonify, request
from flask_security import auth_required, current_user

from extensions import db
from models.company import Company
from models.drive import PlacementDrive
from models.application import Application
from services.company_service import CompanyService
from services.drive_service import DriveService

company_bp = Blueprint(
    "company",
    __name__,
    url_prefix="/api/company"
)


# ============================================================
# Company Dashboard
# ============================================================

@company_bp.route("/dashboard", methods=["GET"])
@auth_required("session")
def dashboard():

    company = Company.query.filter_by(
        user_id=current_user.id
    ).first()

    if company is None:
        return jsonify({
            "message": "Company profile not found."
        }), 404

    drives = PlacementDrive.query.filter_by(company_id=company.id).all()
    total_drives = len(drives)
    active_drives = len([d for d in drives if d.is_active and d.status == "Approved"])
    
    total_applicants = 0
    selected_count = 0
    applicants_list = []

    for drive in drives:
        apps = Application.query.filter_by(drive_id=drive.id).all()
        total_applicants += len(apps)
        selected_count += len([a for a in apps if a.status == "Selected"])
        for app in apps:
            applicants_list.append({
                "id": app.id,
                "name": app.student.full_name if app.student else "Unknown",
                "branch": app.student.branch if app.student else "Unknown",
                "cgpa": app.student.cgpa if app.student else 0.0,
                "status": app.status
            })

    return jsonify({
        "stats": {
            "total_drives": total_drives,
            "active_drives": active_drives,
            "applicants": total_applicants,
            "selected": selected_count
        },
        "drives": [d.to_dict() for d in drives],
        "applicants": applicants_list
    })


# ============================================================
# Company Profile
# ============================================================

@company_bp.route("/profile", methods=["GET"])
@auth_required("session")
def profile():

    company = Company.query.filter_by(
        user_id=current_user.id
    ).first()

    if company is None:
        return jsonify({
            "message": "Company not found."
        }), 404

    return jsonify(company.to_dict())


# ============================================================
# Update Company Profile
# ============================================================

@company_bp.route("/profile", methods=["PUT"])
@auth_required("session")
def update_profile():

    company = Company.query.filter_by(
        user_id=current_user.id
    ).first()

    if company is None:
        return jsonify({
            "message": "Company not found."
        }), 404

    data = request.get_json()
    success, res = CompanyService.update_profile(current_user.id, data)
    if not success:
        return jsonify({"message": res}), 400

    return jsonify({
        "message": "Company profile updated successfully.",
        "company": res.to_dict()
    })


# ============================================================
# Placement Drive Management
# ============================================================

@company_bp.route("/drives/create", methods=["POST"])
@auth_required("session")
def create_drive():
    data = request.get_json()
    # Format deadline date
    from datetime import datetime
    try:
        deadline_str = data.get("application_deadline")
        if deadline_str:
            data["application_deadline"] = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    except Exception as e:
        return jsonify({"message": "Invalid date format. Expected YYYY-MM-DD."}), 400

    success, drive = CompanyService.create_drive(current_user.id, data)
    if not success:
        return jsonify({"message": drive}), 400

    return jsonify({
        "message": "Placement drive created successfully.",
        "drive": drive.to_dict()
    }), 201


@company_bp.route("/drives", methods=["GET"])
@auth_required("session")
def get_company_drives():
    drives = CompanyService.my_drives(current_user.id)
    return jsonify([d.to_dict() for d in drives])


@company_bp.route("/drives/<int:drive_id>", methods=["GET"])
@auth_required("session")
def get_drive_details(drive_id):
    drive = PlacementDrive.query.get_or_404(drive_id)
    # Security check: ensure drive belongs to this company
    company = Company.query.filter_by(user_id=current_user.id).first()
    if not company or drive.company_id != company.id:
        return jsonify({"message": "Unauthorized."}), 403
    return jsonify(drive.to_dict())


@company_bp.route("/drives/<int:drive_id>", methods=["DELETE"])
@auth_required("session")
def delete_drive(drive_id):
    company = Company.query.filter_by(user_id=current_user.id).first()
    drive = PlacementDrive.query.get_or_404(drive_id)
    if not company or drive.company_id != company.id:
        return jsonify({"message": "Unauthorized."}), 403
        
    success, msg = CompanyService.delete_drive(drive_id)
    if not success:
        return jsonify({"message": msg}), 400
    return jsonify({"message": msg})


@company_bp.route("/drives/<int:drive_id>/close", methods=["PUT"])
@auth_required("session")
def close_drive(drive_id):
    company = Company.query.filter_by(user_id=current_user.id).first()
    drive = PlacementDrive.query.get_or_404(drive_id)
    if not company or drive.company_id != company.id:
        return jsonify({"message": "Unauthorized."}), 403

    success, drive_res = DriveService.close(drive_id)
    if not success:
        return jsonify({"message": drive_res}), 400
    return jsonify({"message": "Drive closed successfully.", "drive": drive_res.to_dict()})


# ============================================================
# View Applicants for a Drive
# ============================================================

@company_bp.route("/drives/<int:drive_id>/applicants", methods=["GET"])
@auth_required("session")
def get_applicants(drive_id):
    company = Company.query.filter_by(user_id=current_user.id).first()
    drive = PlacementDrive.query.get_or_404(drive_id)
    if not company or drive.company_id != company.id:
        return jsonify({"message": "Unauthorized."}), 403

    applicants_list = CompanyService.applicants(drive_id)
    data = []
    for app in applicants_list:
        data.append({
            "id": app.id,
            "name": app.student.full_name if app.student else "Unknown",
            "email": app.student.email if app.student else "Unknown",
            "branch": app.student.branch if app.student else "Unknown",
            "cgpa": app.student.cgpa if app.student else 0.0,
            "resume": app.student.resume if app.student else None,
            "status": app.status,
            "interview_date": app.interview_date.strftime("%Y-%m-%d") if app.interview_date else None
        })
    return jsonify(data)


# ============================================================
# Application Actions (Status, Shortlist, Reject, Select, Interview)
# ============================================================

@company_bp.route("/application/<int:application_id>/status", methods=["PUT"])
@auth_required("session")
def update_application_status(application_id):
    data = request.get_json()
    status = data.get("status")
    success, res = CompanyService.update_status(application_id, status)
    if not success:
        return jsonify({"message": res}), 400
    return jsonify({"message": "Status updated successfully.", "application": res.to_dict()})


@company_bp.route("/application/<int:application_id>/shortlist", methods=["PUT"])
@auth_required("session")
def shortlist_student(application_id):
    success, res = CompanyService.update_status(application_id, "Shortlisted")
    if not success:
        return jsonify({"message": res}), 400
    return jsonify({"message": "Student shortlisted successfully."})


@company_bp.route("/application/<int:application_id>/reject", methods=["PUT"])
@auth_required("session")
def reject_student(application_id):
    success, res = CompanyService.update_status(application_id, "Rejected")
    if not success:
        return jsonify({"message": res}), 400
    return jsonify({"message": "Student rejected successfully."})


@company_bp.route("/application/<int:application_id>/select", methods=["PUT"])
@auth_required("session")
def select_student(application_id):
    success, res = CompanyService.update_status(application_id, "Selected")
    if not success:
        return jsonify({"message": res}), 400
    return jsonify({"message": "Student selected successfully."})


@company_bp.route("/application/<int:application_id>/interview", methods=["PUT"])
@auth_required("session")
def schedule_interview(application_id):
    data = request.get_json()
    interview_date_str = data.get("interview_date")
    from datetime import datetime
    try:
        interview_date = datetime.strptime(interview_date_str, "%Y-%m-%dT%H:%M")
    except Exception:
        try:
            interview_date = datetime.strptime(interview_date_str, "%Y-%m-%d")
        except Exception:
            return jsonify({"message": "Invalid date format."}), 400

    success, res = CompanyService.schedule_interview(application_id, interview_date)
    if not success:
        return jsonify({"message": res}), 400
    return jsonify({"message": "Interview scheduled successfully.", "application": res.to_dict()})