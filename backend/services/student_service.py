# backend/services/student_service.py

from extensions import db
from models.student import Student
from models.application import Application
from models.drive import PlacementDrive


class StudentService:

    # ==========================================
    # Get Student Profile
    # ==========================================

    @staticmethod
    def get_profile(user_id):

        return Student.query.filter_by(
            user_id=user_id
        ).first()

    # ==========================================
    # Update Profile
    # ==========================================

    @staticmethod
    def update_profile(user_id, data):

        student = Student.query.filter_by(
            user_id=user_id
        ).first()

        if student is None:
            return False, "Student not found."

        student.full_name = data.get(
            "full_name",
            student.full_name
        )

        student.phone = data.get(
            "phone",
            student.phone
        )

        student.branch = data.get(
            "branch",
            student.branch
        )

        student.year = data.get(
            "year",
            student.year
        )

        student.cgpa = data.get(
            "cgpa",
            student.cgpa
        )

        student.skills = data.get(
            "skills",
            student.skills
        )

        student.address = data.get(
            "address",
            student.address
        )

        db.session.commit()

        return True, student

    # ==========================================
    # Dashboard
    # ==========================================

    @staticmethod
    def dashboard(user_id):

        student = Student.query.filter_by(
            user_id=user_id
        ).first()

        if student is None:
            return None

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

        return {

            "student_name": student.full_name,

            "branch": student.branch,

            "cgpa": student.cgpa,

            "approved_drives": approved_drives,

            "applications": total_applications,

            "shortlisted": shortlisted,

            "selected": selected

        }

    # ==========================================
    # Eligible Drives
    # ==========================================

    @staticmethod
    def eligible_drives(user_id):

        student = Student.query.filter_by(
            user_id=user_id
        ).first()

        if student is None:
            return []

        return PlacementDrive.query.filter(

            PlacementDrive.status == "Approved",

            PlacementDrive.is_active == True,

            PlacementDrive.eligible_branch == student.branch,

            PlacementDrive.eligible_year == student.year,

            PlacementDrive.minimum_cgpa <= student.cgpa

        ).all()

    # ==========================================
    # Application History
    # ==========================================

    @staticmethod
    def application_history(user_id):

        student = Student.query.filter_by(
            user_id=user_id
        ).first()

        if student is None:
            return []

        return Application.query.filter_by(
            student_id=student.id
        ).all()

    # ==========================================
    # Placement History
    # ==========================================

    @staticmethod
    def placement_history(user_id):

        student = Student.query.filter_by(
            user_id=user_id
        ).first()

        if student is None:
            return []

        return Application.query.filter(

            Application.student_id == student.id,

            Application.status == "Selected"

        ).all()

    # ==========================================
    # Upload Resume
    # ==========================================

    @staticmethod
    def upload_resume(user_id, filename):

        student = Student.query.filter_by(
            user_id=user_id
        ).first()

        if student is None:
            return False, "Student not found."

        student.resume = filename

        db.session.commit()

        return True, filename

    # ==========================================
    # Blacklist Student
    # ==========================================

    @staticmethod
    def blacklist(student_id):

        student = Student.query.get(student_id)

        if student is None:
            return False, "Student not found."

        student.is_blacklisted = True

        db.session.commit()

        return True, student

    # ==========================================
    # Activate Student
    # ==========================================

    @staticmethod
    def activate(student_id):

        student = Student.query.get(student_id)

        if student is None:
            return False, "Student not found."

        student.is_blacklisted = False
        student.is_active = True

        db.session.commit()

        return True, student

    # ==========================================
    # Search Students
    # ==========================================

    @staticmethod
    def search(keyword):

        return Student.query.filter(

            Student.full_name.ilike(
                f"%{keyword}%"
            )

        ).all()

    # ==========================================
    # Total Students
    # ==========================================

    @staticmethod
    def total_students():

        return Student.query.count()

    # ==========================================
    # Active Students
    # ==========================================

    @staticmethod
    def active_students():

        return Student.query.filter_by(
            is_active=True
        ).count()

    # ==========================================
    # Blacklisted Students
    # ==========================================

    @staticmethod
    def blacklisted_students():

        return Student.query.filter_by(
            is_blacklisted=True
        ).count()

    # ==========================================
    # Get Student By ID
    # ==========================================

    @staticmethod
    def get(student_id):

        return Student.query.get(student_id)