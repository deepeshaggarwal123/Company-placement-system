# backend/services/auth_service.py

import uuid

from flask_security.utils import hash_password, verify_password

from extensions import db, user_datastore

from models.user import User
from models.role import Role
from models.student import Student
from models.company import Company


class AuthService:

    # ---------------------------------------------
    # Login
    # ---------------------------------------------

    @staticmethod
    def login(email, password):

        user = User.query.filter_by(
            email=email
        ).first()

        if user is None:
            return False, "Invalid Email"

        if not verify_password(password, user.password):
            return False, "Invalid Password"

        if not user.active:
            return False, "Account is inactive"

        return True, user

    # ---------------------------------------------
    # Register Student
    # ---------------------------------------------

    @staticmethod
    def register_student(data):
        try:
            email = data.get("email")

            if not email:
                return False, "Email is required."

            if User.query.filter_by(email=email).first():
                return False, "Email already exists."

            role = Role.query.filter_by(name="student").first()
            if role is None:
                role = user_datastore.create_role(name="student", description="Student User")
                db.session.commit()

            user = user_datastore.create_user(
                email=email,
                password=hash_password(data["password"]),
                active=True,
                fs_uniquifier=str(uuid.uuid4())
            )

            user.roles.append(role)

            student = Student(
                user=user,
                full_name=data.get("full_name", ""),
                enrollment_no=data.get("enrollment_no", ""),
                email=email,
                phone=data.get("phone", ""),
                branch=data.get("branch", ""),
                year=data.get("year", 1),
                cgpa=data.get("cgpa", 0.0)
            )

            db.session.add(student)
            db.session.commit()

            return True, student

        except Exception as e:
            db.session.rollback()
            return False, f"Registration failed: {str(e)}"


    # ---------------------------------------------
    # Register Company
    # ---------------------------------------------

    @staticmethod
    def register_company(data):
        try:
            email = data.get("email")

            if not email:
                return False, "HR Email (used as login) is required."

            if User.query.filter_by(email=email).first():
                return False, "Email already exists."

            role = Role.query.filter_by(name="company").first()
            if role is None:
                role = user_datastore.create_role(name="company", description="Company User")
                db.session.commit()

            user = user_datastore.create_user(
                email=email,
                password=hash_password(data["password"]),
                active=True,
                fs_uniquifier=str(uuid.uuid4())
            )

            user.roles.append(role)

            company = Company(
                user=user,
                company_name=data.get("company_name", ""),
                hr_name=data.get("hr_name", ""),
                hr_email=data.get("hr_email", email),
                hr_phone=data.get("hr_phone", ""),
                website=data.get("website", ""),
                industry=data.get("industry", ""),
                approval_status="Pending"
            )

            db.session.add(company)
            db.session.commit()

            return True, company

        except Exception as e:
            db.session.rollback()
            return False, f"Registration failed: {str(e)}"


    # ---------------------------------------------
    # Get User
    # ---------------------------------------------

    @staticmethod
    def get_user(user_id):

        return User.query.get(user_id)

    # ---------------------------------------------
    # Deactivate User
    # ---------------------------------------------

    @staticmethod
    def deactivate(user_id):

        user = User.query.get(user_id)

        if user is None:
            return False

        user.active = False

        db.session.commit()

        return True