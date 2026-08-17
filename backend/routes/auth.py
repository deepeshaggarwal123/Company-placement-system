# backend/routes/auth.py

import uuid

from flask import Blueprint, request, jsonify
from flask_security import (
    login_user,
    logout_user,
    current_user,
    auth_required
)
from flask_security.utils import verify_password, hash_password

from extensions import db, user_datastore

from models.user import User
from models.student import Student
from models.company import Company
from models.role import Role

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


# =====================================================
# LOGIN
# =====================================================

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and Password are required."
        }), 400

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({
            "message": "Invalid Email or Password."
        }), 401

    if not verify_password(password, user.password):
        return jsonify({
            "message": "Invalid Email or Password."
        }), 401

    if not user.active:
        return jsonify({
            "message": "Account is inactive."
        }), 403

    login_user(user)

    # Return fs_uniquifier as the token so frontend can store it
    return jsonify({
        "message": "Login Successful",
        "token": user.fs_uniquifier,
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    })


# =====================================================
# REGISTER STUDENT
# =====================================================

@auth_bp.route("/student/register", methods=["POST"])
def register_student():
    from services.auth_service import AuthService
    data = request.get_json()
    
    # Map frontend keys to backend names
    if "full_name" not in data and "name" in data:
        data["full_name"] = data["name"]
    if "enrollment_no" not in data and "roll_no" in data:
        data["enrollment_no"] = data["roll_no"]
        
    success, student = AuthService.register_student(data)
    if not success:
        return jsonify({"message": student}), 400
    
    return jsonify({
        "message": "Student registered successfully",
        "student": student.to_dict()
    }), 201


# =====================================================
# REGISTER COMPANY
# =====================================================

@auth_bp.route("/company/register", methods=["POST"])
def register_company():
    from services.auth_service import AuthService
    data = request.get_json()
    
    # Map frontend keys to backend names
    if "email" not in data and "hr_email" in data:
        data["email"] = data["hr_email"]
        
    success, company = AuthService.register_company(data)
    if not success:
        return jsonify({"message": company}), 400

    return jsonify({
        "message": "Company registered successfully",
        "company": company.to_dict()
    }), 201


# =====================================================
# CHANGE PASSWORD
# =====================================================

@auth_bp.route("/change-password", methods=["PUT"])
@auth_required("session")
def change_password():
    data = request.get_json()
    old_password = data.get("old_password")
    new_password = data.get("new_password")
    
    if not verify_password(old_password, current_user.password):
        return jsonify({"message": "Invalid old password."}), 400
        
    current_user.password = hash_password(new_password)
    db.session.commit()
    return jsonify({"message": "Password changed successfully."})


# =====================================================
# FORGOT PASSWORD
# =====================================================

@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    email = data.get("email")
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"message": "User not found."}), 404
        
    # In a real app we'd send an email. For this course project, we return success.
    return jsonify({"message": "Password reset instructions sent to your email."})


# =====================================================
# RESET PASSWORD
# =====================================================

@auth_bp.route("/reset-password/<token>", methods=["POST"])
def reset_password(token):
    data = request.get_json()
    password = data.get("password")
    # For course project simplicity, reset password using token (user.fs_uniquifier as token)
    user = User.query.filter_by(fs_uniquifier=token).first()
    if not user:
        return jsonify({"message": "Invalid or expired token."}), 400
        
    user.password = hash_password(password)
    db.session.commit()
    return jsonify({"message": "Password reset successfully."})


# =====================================================
# LOGOUT
# =====================================================

@auth_bp.route("/logout", methods=["POST"])
@auth_required("session")
def logout():

    logout_user()

    return jsonify({
        "message": "Logged out successfully."
    })


# =====================================================
# CURRENT USER
# =====================================================

@auth_bp.route("/me", methods=["GET"])
@auth_required("session")
def me():

    return jsonify({

        "id": current_user.id,

        "email": current_user.email,

        "role": current_user.role

    })