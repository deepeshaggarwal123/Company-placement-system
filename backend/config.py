import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads", "resumes")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")

os.makedirs(INSTANCE_DIR, exist_ok=True)

if os.path.exists(UPLOAD_DIR) and not os.path.isdir(UPLOAD_DIR):
    os.remove(UPLOAD_DIR)
os.makedirs(UPLOAD_DIR, exist_ok=True)

if os.path.exists(EXPORT_DIR) and not os.path.isdir(EXPORT_DIR):
    os.remove(EXPORT_DIR)
os.makedirs(EXPORT_DIR, exist_ok=True)


class Config:
    """Base Configuration"""

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "placement_portal_secret_key")

    # SQLite Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(INSTANCE_DIR, "placement.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Configuration
    UPLOAD_FOLDER = UPLOAD_DIR
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB

    # Flask-Security
    SECURITY_PASSWORD_SALT = os.getenv(
        "SECURITY_PASSWORD_SALT",
        "placement_password_salt"
    )

    SECURITY_REGISTERABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_RECOVERABLE = False
    SECURITY_CONFIRMABLE = False
    SECURITY_TRACKABLE = False
    SECURITY_CHANGEABLE = True

    # Flask-Caching (SimpleCache - no Redis required)
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300

    # Celery (disabled when Redis not available)
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

    # Mail Configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME", "")

    # Session
    SESSION_PERMANENT = False

    # Timezone
    TIMEZONE = "Asia/Kolkata"

    # CSV Export Folder
    EXPORT_FOLDER = EXPORT_DIR

    # Allowed Resume Extensions
    ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

    # Pagination
    STUDENTS_PER_PAGE = 10
    COMPANIES_PER_PAGE = 10
    DRIVES_PER_PAGE = 10

    # Default Admin
    ADMIN_EMAIL = "admin@placement.com"
    ADMIN_PASSWORD = "Admin@123"

    # Placement Status
    DRIVE_STATUS = [
        "Pending",
        "Approved",
        "Rejected",
        "Closed",
    ]

    APPLICATION_STATUS = [
        "Applied",
        "Shortlisted",
        "Selected",
        "Rejected",
    ]

    COMPANY_STATUS = [
        "Pending",
        "Approved",
        "Rejected",
        "Blacklisted",
    ]