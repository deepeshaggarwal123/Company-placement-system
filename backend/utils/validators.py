# backend/utils/validators.py

import re
from datetime import datetime


# ==========================================================
# Email Validation
# ==========================================================

def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(
        pattern,
        email
    ) is not None



# ==========================================================
# Password Validation
# ==========================================================

def validate_password(password):

    """
    Minimum:
    - 8 characters
    - One uppercase
    - One lowercase
    - One digit
    """

    if len(password) < 8:
        return False


    if not re.search(
        r"[A-Z]",
        password
    ):
        return False


    if not re.search(
        r"[a-z]",
        password
    ):
        return False


    if not re.search(
        r"[0-9]",
        password
    ):
        return False


    return True



# ==========================================================
# Phone Number Validation
# ==========================================================

def validate_phone(phone):

    pattern = r'^[6-9]\d{9}$'

    return re.match(
        pattern,
        str(phone)
    ) is not None



# ==========================================================
# Student Validation
# ==========================================================

def validate_student(data):

    required_fields = [

        "full_name",
        "email",
        "password",
        "enrollment_no",
        "branch",
        "year",
        "cgpa"

    ]


    for field in required_fields:

        if not data.get(field):

            return False, f"{field} is required"



    if not validate_email(
        data["email"]
    ):

        return False, "Invalid email"



    if not validate_password(
        data["password"]
    ):

        return False, "Weak password"



    if float(data["cgpa"]) < 0 or float(data["cgpa"]) > 10:

        return False, "Invalid CGPA"



    return True, "Valid Student"



# ==========================================================
# Company Validation
# ==========================================================

def validate_company(data):

    required_fields = [

        "company_name",

        "hr_name",

        "hr_email",

        "hr_phone",

        "password"

    ]


    for field in required_fields:

        if not data.get(field):

            return False, f"{field} is required"



    if not validate_email(
        data["hr_email"]
    ):

        return False, "Invalid HR email"



    if not validate_phone(
        data["hr_phone"]
    ):

        return False, "Invalid phone number"



    if not validate_password(
        data["password"]
    ):

        return False, "Weak password"



    return True, "Valid Company"



# ==========================================================
# Placement Drive Validation
# ==========================================================

def validate_drive(data):

    required_fields = [

        "job_title",

        "job_description",

        "eligible_branch",

        "eligible_year",

        "minimum_cgpa",

        "application_deadline"

    ]


    for field in required_fields:

        if not data.get(field):

            return False, f"{field} is required"



    if float(data["minimum_cgpa"]) < 0:

        return False, "Invalid CGPA"



    try:

        deadline = datetime.strptime(

            str(data["application_deadline"]),

            "%Y-%m-%d"

        )


        if deadline.date() < datetime.today().date():

            return False, "Deadline cannot be past"



    except:

        return False, "Invalid date format"



    return True, "Valid Drive"



# ==========================================================
# Application Validation
# ==========================================================

def validate_application(student, drive):

    if student is None:

        return False, "Student not found"


    if drive is None:

        return False, "Drive not found"



    if drive.status != "Approved":

        return False, "Drive not approved"



    if student.branch != drive.eligible_branch:

        return False, "Branch not eligible"



    if student.year != drive.eligible_year:

        return False, "Year not eligible"



    if student.cgpa < drive.minimum_cgpa:

        return False, "CGPA criteria not matched"



    return True, "Eligible"



# ==========================================================
# File Validation
# ==========================================================

def validate_file(filename):

    allowed_extensions = [

        "pdf",

        "doc",

        "docx"

    ]


    if "." not in filename:

        return False


    extension = filename.rsplit(
        ".",
        1
    )[1].lower()


    return extension in allowed_extensions



# ==========================================================
# URL Validation
# ==========================================================

def validate_url(url):

    pattern = (
        r'^(https?://)?'
        r'([\da-z\.-]+)\.'
        r'([a-z\.]{2,6})'
    )


    return re.match(
        pattern,
        url
    ) is not None