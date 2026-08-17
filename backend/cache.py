# backend/cache.py

from flask_caching import Cache

# Cache instance
cache = Cache()


def init_cache(app):
    """
    Initialize Redis cache with Flask app.
    """
    cache.init_app(app)


# -------------------------------
# Cache Keys
# -------------------------------

ADMIN_DASHBOARD = "admin_dashboard"
STUDENT_DASHBOARD = "student_dashboard_{}"
COMPANY_DASHBOARD = "company_dashboard_{}"
APPROVED_DRIVES = "approved_drives"
ALL_COMPANIES = "all_companies"
ALL_STUDENTS = "all_students"


# -------------------------------
# Cache Helper Functions
# -------------------------------

def clear_admin_dashboard():
    cache.delete(ADMIN_DASHBOARD)


def clear_student_dashboard(student_id):
    cache.delete(STUDENT_DASHBOARD.format(student_id))


def clear_company_dashboard(company_id):
    cache.delete(COMPANY_DASHBOARD.format(company_id))


def clear_all():
    """
    Clear all Redis cache.
    """
    cache.clear()