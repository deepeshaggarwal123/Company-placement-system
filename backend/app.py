from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, security, cache, mail, create_default_roles, create_default_admin

# Blueprints
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.student import student_bp
from routes.company import company_bp
from routes.drive import drive_bp
from routes.application import application_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions
    from extensions import init_extensions
    init_extensions(app)

    CORS(app, origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5000",
    ], supports_credentials=True)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(student_bp, url_prefix="/api/student")
    app.register_blueprint(company_bp, url_prefix="/api/company")
    app.register_blueprint(drive_bp, url_prefix="/api/drives")
    app.register_blueprint(application_bp, url_prefix="/api/application")

    @app.route("/")
    def home():
        return {
            "application": "Placement Portal Application",
            "version": "1.0",
            "status": "Running"
        }

    with app.app_context():
        db.create_all()
        create_default_roles()
        create_default_admin(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)