# backend/models/__init__.py

from .role import Role
from .user import User
from .student import Student
from .company import Company
from .drive import PlacementDrive
from .application import Application

__all__ = [
    "Role",
    "User",
    "Student",
    "Company",
    "PlacementDrive",
    "Application",
]