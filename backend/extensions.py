# backend/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_security.utils import hash_password

# -------------------------------------
# Database
# -------------------------------------
db = SQLAlchemy()

# -------------------------------------
# Database Migration
# -------------------------------------
migrate = Migrate()

# -------------------------------------
# Flask Security
# -------------------------------------
security = Security()
user_datastore = None

# -------------------------------------
# Redis Cache
# -------------------------------------
cache = Cache()

# -------------------------------------
# Mail
# -------------------------------------
mail = Mail()


def init_extensions(app):
    """
    Initialize all Flask extensions.
    """

    global user_datastore

    # Database
    db.init_app(app)

    # Migration
    migrate.init_app(app, db)

    # Cache
    cache.init_app(app)

    # Mail
    mail.init_app(app)

    # Import models here to avoid circular imports
    from models.user import User
    from models.role import Role

    # Flask-Security datastore
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    # Initialize Flask-Security
    security.init_app(app, user_datastore)

    return app


def create_default_roles():
    """
    Create default roles if they don't exist.
    """

    roles = [
        ("admin", "Institute Administrator"),
        ("student", "Student User"),
        ("company", "Company User"),
    ]

    for name, description in roles:
        role = user_datastore.find_role(name)

        if role is None:
            user_datastore.create_role(
                name=name,
                description=description
            )

    db.session.commit()


def create_default_admin(app):
    """
    Create default admin after database creation.
    """

    with app.app_context():

        admin = user_datastore.find_user(
            email=app.config["ADMIN_EMAIL"]
        )

        if admin is None:

            admin = user_datastore.create_user(
                email=app.config["ADMIN_EMAIL"],
                password=hash_password(
                    app.config["ADMIN_PASSWORD"]
                ),
                active=True
            )

            user_datastore.add_role_to_user(admin, "admin")

            db.session.commit()

            print("✅ Default Admin Created")
        else:
            print("ℹ️ Admin already exists")