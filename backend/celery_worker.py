# backend/celery_worker.py

from celery import Celery
from celery.schedules import crontab
from app import create_app

# Create Flask App
flask_app = create_app()


def make_celery(app):

    celery = Celery(
        app.import_name,
        broker=app.config["CELERY_BROKER_URL"],
        backend=app.config["CELERY_RESULT_BACKEND"]
    )

    # Celery Configuration
    celery.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        result_backend=app.config["CELERY_RESULT_BACKEND"],
        timezone="Asia/Kolkata",
        enable_utc=False
    )

    # Flask Context for Celery Tasks
    class ContextTask(celery.Task):

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    # -----------------------------
    # Celery Beat Schedule
    # -----------------------------
    celery.conf.beat_schedule = {

        "daily-reminder": {
            "task": "tasks.daily_reminder",
            "schedule": crontab(hour=9, minute=0),
        },

        "monthly-report": {
            "task": "tasks.monthly_report",
            "schedule": crontab(day_of_month=1, hour=8, minute=0),
        },

        "clear-cache": {
            "task": "tasks.clear_cache",
            "schedule": crontab(hour=0, minute=0),
        },
    }

    return celery


# Celery Instance
celery = make_celery(flask_app)

# Import Tasks AFTER Celery initialization
import tasks