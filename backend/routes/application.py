# backend/routes/application.py

from flask import Blueprint, request, jsonify
from flask_security import auth_required, current_user

from extensions import db
from models.student import Student
from models.drive import PlacementDrive
from models.application import Application

application_bp = Blueprint(
    "application",
    __name__,
    url_prefix="/api/applications"
)


# ============================================================
# Apply for a Placement Drive
# ============================================================

@application_bp.route("/apply/<int:drive_id>", methods=["POST"])
@auth_required("session")
def apply_drive(drive_id):

    student = Student.query.filter_by(
        user_id=current_user.id
    ).first()

    if not student:
        return jsonify({
            "message": "Student profile not found."
        }), 404

    drive = PlacementDrive.query.get(drive_id)

    if not drive:
        return jsonify({
            "message": "Placement Drive not found."
        }), 404

    if drive.status != "Approved":
        return jsonify({
            "message": "Drive is not approved."
        }), 400

    # Check eligibility
    if student.branch != drive.eligible_branch:
        return jsonify({
            "message": "Branch not eligible."
        }), 400

    if student.cgpa < drive.minimum_cgpa:
        return jsonify({
            "message": "CGPA requirement not met."
        }), 400

    if student.year != drive.eligible_year:
        return jsonify({
            "message": "Year not eligible."
        }), 400

    # Prevent duplicate application
    existing = Application.query.filter_by(
        student_id=student.id,
        drive_id=drive.id
    ).first()

    if existing:
        return jsonify({
            "message": "Already applied."
        }), 400

    application = Application(
        student_id=student.id,
        drive_id=drive.id,
        status="Applied"
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "message": "Application submitted successfully."
    }), 201


# ============================================================
# Student Application History
# ============================================================

@application_bp.route("/my-applications", methods=["GET"])
@auth_required("session")
def my_applications():

    student = Student.query.filter_by(
        user_id=current_user.id
    ).first()

    applications = Application.query.filter_by(
        student_id=student.id
    ).all()

    data = []

    for app in applications:

        data.append({

            "application_id": app.id,

            "company": app.drive.company.company_name,

            "job_title": app.drive.job_title,

            "status": app.status,

            "application_date": app.application_date,

            "interview_date": app.interview_date

        })

    return jsonify(data)


# ============================================================
# Company - View Applicants
# ============================================================

@application_bp.route("/drive/<int:drive_id>", methods=["GET"])
@auth_required("session")
def drive_applications(drive_id):

    applications = Application.query.filter_by(
        drive_id=drive_id
    ).all()

    data = []

    for app in applications:

        data.append({

            "application_id": app.id,

            "student_name": app.student.full_name,

            "email": app.student.email,

            "cgpa": app.student.cgpa,

            "branch": app.student.branch,

            "status": app.status

        })

    return jsonify(data)


# ============================================================
# Update Application Status
# ============================================================

@application_bp.route(
    "/update-status/<int:application_id>",
    methods=["PUT"]
)
@auth_required("session")
def update_status(application_id):

    application = Application.query.get(application_id)

    if not application:
        return jsonify({
            "message": "Application not found."
        }), 404

    data = request.get_json()

    status = data.get("status")

    allowed = [
        "Applied",
        "Shortlisted",
        "Selected",
        "Rejected"
    ]

    if status not in allowed:
        return jsonify({
            "message": "Invalid status."
        }), 400

    application.status = status

    db.session.commit()

    return jsonify({
        "message": "Status updated successfully."
    })


# ============================================================
# Delete Application
# ============================================================

@application_bp.route("/<int:application_id>", methods=["DELETE"])
@auth_required("session")
def delete_application(application_id):

    application = Application.query.get(application_id)

    if not application:
        return jsonify({
            "message": "Application not found."
        }), 404

    db.session.delete(application)
    db.session.commit()

    return jsonify({
        "message": "Application deleted successfully."
    })