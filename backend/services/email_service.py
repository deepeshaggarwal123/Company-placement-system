# backend/services/email_service.py

from flask import render_template
from flask_mail import Message

from extensions import mail


class EmailService:

    # =====================================================
    # Send Simple Email
    # =====================================================

    @staticmethod
    def send_email(subject, recipients, body):

        try:
            msg = Message(
                subject=subject,
                recipients=recipients
            )

            msg.body = body

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False

    # =====================================================
    # Send HTML Email
    # =====================================================

    @staticmethod
    def send_html_email(subject, recipients, template, **kwargs):

        try:

            html = render_template(
                template,
                **kwargs
            )

            msg = Message(
                subject=subject,
                recipients=recipients
            )

            msg.html = html

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False

    # =====================================================
    # Daily Reminder
    # =====================================================

    @staticmethod
    def send_daily_reminder(student, drives):

        try:

            html = render_template(

                "reminder_mail.html",

                student=student,

                drives=drives

            )

            msg = Message(

                subject="Placement Drive Reminder",

                recipients=[student.email]

            )

            msg.html = html

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False

    # =====================================================
    # Monthly Admin Report
    # =====================================================

    @staticmethod
    def send_monthly_report(admin_email, report):

        try:

            html = render_template(

                "monthly_report.html",

                report=report

            )

            msg = Message(

                subject="Monthly Placement Report",

                recipients=[admin_email]

            )

            msg.html = html

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False

    # =====================================================
    # Selection Mail
    # =====================================================

    @staticmethod
    def send_selection_mail(student, drive):

        try:

            msg = Message(

                subject="Congratulations! You are Selected",

                recipients=[student.email]

            )

            msg.body = f"""
Dear {student.full_name},

Congratulations!

You have been selected for the position of

{drive.job_title}

Company:
{drive.company.company_name}

Please login to the Placement Portal
for further instructions.

Regards
Placement Cell
"""

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False

    # =====================================================
    # Interview Schedule Mail
    # =====================================================

    @staticmethod
    def send_interview_mail(
            student,
            drive,
            interview_date
    ):

        try:

            msg = Message(

                subject="Interview Scheduled",

                recipients=[student.email]

            )

            msg.body = f"""
Dear {student.full_name},

Your interview has been scheduled.

Company:
{drive.company.company_name}

Job Title:
{drive.job_title}

Interview Date:
{interview_date}

Best Wishes!

Placement Cell
"""

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False

    # =====================================================
    # Company Approval Mail
    # =====================================================

    @staticmethod
    def company_approved(company):

        try:

            msg = Message(

                subject="Company Approved",

                recipients=[company.hr_email]

            )

            msg.body = f"""
Dear {company.company_name},

Your company registration has been approved.

You can now login and create
placement drives.

Regards
Placement Cell
"""

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False

    # =====================================================
    # Company Rejection Mail
    # =====================================================

    @staticmethod
    def company_rejected(company):

        try:

            msg = Message(

                subject="Company Registration Rejected",

                recipients=[company.hr_email]

            )

            msg.body = f"""
Dear {company.company_name},

Unfortunately your company registration
has been rejected by the Placement Cell.

For more information,
please contact the administrator.

Regards
Placement Cell
"""

            mail.send(msg)

            return True

        except Exception as e:
            print(e)
            return False