# backend/utils/reminder_mail.py

from flask import render_template
from flask_mail import Message

from extensions import mail


def send_reminder_email(student, drives):
    """
    Send daily reminder email to a student.
    """

    try:

        html = render_template(
            "reminder_mail.html",
            student=student,
            drives=drives
        )

        msg = Message(
            subject="Placement Portal - Daily Reminder",
            recipients=[student.email]
        )

        msg.html = html

        mail.send(msg)

        return True

    except Exception as e:
        print("Reminder Mail Error:", e)
        return False