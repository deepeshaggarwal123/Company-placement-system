# backend/create_db.py

from app import create_app
from extensions import db
from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import hash_password
from models.user import User
from models.role import Role

app = create_app()

# Flask-Security User Datastore
user_datastore = SQLAlchemyUserDatastore(db, User, Role)


def create_roles():
    """Create default roles."""
    roles = ["admin", "student", "company"]
    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            user_datastore.create_role(
                name=role_name,
                description=f"{role_name.capitalize()} Role"
            )
    db.session.commit()
    print("[OK] Roles Created")


def create_admin():
    """Create default admin with hashed password."""
    admin_email = app.config["ADMIN_EMAIL"]
    admin_password = app.config["ADMIN_PASSWORD"]

    admin = User.query.filter_by(email=admin_email).first()
    if admin:
        print("[OK] Admin already exists")
        return

    admin = user_datastore.create_user(
        email=admin_email,
        password=hash_password(admin_password),
        active=True
    )
    admin_role = Role.query.filter_by(name="admin").first()
    user_datastore.add_role_to_user(admin, admin_role)
    db.session.commit()

    print("[OK] Default Hashed Admin Created")
    print(f"Email    : {admin_email}")
    print(f"Password : {admin_password}")


def create_database():
    """Create database tables."""
    with app.app_context():
        db.create_all()
        print("[OK] Database Created")
        create_roles()
        create_admin()
        print("[OK] Placement Portal Setup Complete")


if __name__ == "__main__":
    create_database()