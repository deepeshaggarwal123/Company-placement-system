# backend/utils/mail.py

from flask_mail import Message

from extensions import mail


# ==========================================================
# Send Plain Text Email
# ==========================================================

def send_mail(
        subject,
        recipient,
        body
):

    try:

        msg = Message(

            subject=subject,

            recipients=[recipient]

        )

        msg.body = body


        mail.send(msg)

        return True


    except Exception as e:

        print(
            "Mail Error:",
            e
        )

        return False



# ==========================================================
# Send HTML Email
# ==========================================================

def send_html_mail(
        subject,
        recipient,
        html_content
):

    try:

        msg = Message(

            subject=subject,

            recipients=[recipient]

        )

        msg.html = html_content


        mail.send(msg)

        return True


    except Exception as e:

        print(
            "HTML Mail Error:",
            e
        )

        return False



# ==========================================================
# Send Multiple Recipients
# ==========================================================

def send_bulk_mail(
        subject,
        recipients,
        body
):

    try:

        msg = Message(

            subject=subject,

            recipients=recipients

        )


        msg.body = body


        mail.send(msg)


        return True


    except Exception as e:

        print(
            "Bulk Mail Error:",
            e
        )

        return False



# ==========================================================
# Send Placement Selection Mail
# ==========================================================

def send_selection_email(
        student,
        company,
        drive
):

    subject = "Placement Selection Confirmation"


    body = f"""
Dear {student.full_name},

Congratulations!

You have been selected for the placement drive.

Company:
{company.company_name}

Role:
{drive.job_title}


Please check your Placement Portal dashboard
for further details.

Regards,
Placement Cell
"""


    return send_mail(

        subject,

        student.email,

        body

    )



# ==========================================================
# Send Interview Schedule Mail
# ==========================================================

def send_interview_email(
        student,
        company,
        drive,
        interview_date
):

    subject = "Interview Scheduled"


    body = f"""
Dear {student.full_name},

Your interview has been scheduled.

Company:
{company.company_name}

Job Role:
{drive.job_title}

Interview Date:
{interview_date}


Best Wishes.

Placement Cell
"""


    return send_mail(

        subject,

        student.email,

        body

    )



# ==========================================================
# Send Company Approval Mail
# ==========================================================

def send_company_approval_email(company):

    subject = "Company Registration Approved"


    body = f"""
Dear {company.company_name},

Your company registration has been approved
by the Placement Cell.

You can now create placement drives
through the Placement Portal.

Regards,
Placement Cell
"""


    return send_mail(

        subject,

        company.hr_email,

        body

    )



# ==========================================================
# Send Company Rejection Mail
# ==========================================================

def send_company_rejection_email(company):

    subject = "Company Registration Rejected"


    body = f"""
Dear {company.company_name},

Your company registration request
has been rejected.

Please contact the Placement Cell
for more details.

Regards,
Placement Cell
"""


    return send_mail(

        subject,

        company.hr_email,

        body

    )