# backend/utils/decorators.py

from functools import wraps

from flask import jsonify

from flask_security import current_user


# ==========================================================
# Login Required
# ==========================================================

def login_required_api(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

            return jsonify({
                "success": False,
                "message": "Login required."
            }), 401

        return func(*args, **kwargs)

    return wrapper


# ==========================================================
# Admin Required
# ==========================================================

def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

            return jsonify({
                "success": False,
                "message": "Login required."
            }), 401

        if not current_user.has_role("admin"):

            return jsonify({
                "success": False,
                "message": "Admin access only."
            }), 403

        return func(*args, **kwargs)

    return wrapper


# ==========================================================
# Student Required
# ==========================================================

def student_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

            return jsonify({
                "success": False,
                "message": "Login required."
            }), 401

        if not current_user.has_role("student"):

            return jsonify({
                "success": False,
                "message": "Student access only."
            }), 403

        return func(*args, **kwargs)

    return wrapper


# ==========================================================
# Company Required
# ==========================================================

def company_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

            return jsonify({
                "success": False,
                "message": "Login required."
            }), 401

        if not current_user.has_role("company"):

            return jsonify({
                "success": False,
                "message": "Company access only."
            }), 403

        return func(*args, **kwargs)

    return wrapper


# ==========================================================
# Active Account Required
# ==========================================================

def active_user_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.active:

            return jsonify({
                "success": False,
                "message": "Your account has been deactivated."
            }), 403

        return func(*args, **kwargs)

    return wrapper


# ==========================================================
# Approved Company Required
# ==========================================================

def approved_company_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.has_role("company"):

            return jsonify({
                "success": False,
                "message": "Company access only."
            }), 403

        company = current_user.company

        if company.approval_status != "Approved":

            return jsonify({
                "success": False,
                "message": "Company is not approved by Admin."
            }), 403

        return func(*args, **kwargs)

    return wrapper


# ==========================================================
# Not Blacklisted Student
# ==========================================================

def student_not_blacklisted(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.has_role("student"):

            student = current_user.student

            if student.is_blacklisted:

                return jsonify({
                    "success": False,
                    "message": "Student account is blacklisted."
                }), 403

        return func(*args, **kwargs)

    return wrapper