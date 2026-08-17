# backend/utils/helper.py

import os
import uuid
from datetime import datetime

from werkzeug.utils import secure_filename


# ==========================================================
# Generate Unique Filename
# ==========================================================

def generate_filename(filename):
    """
    Generate unique filename for uploads.
    """

    ext = filename.rsplit(".", 1)[1].lower()

    new_filename = (
        str(uuid.uuid4())
        + "."
        + ext
    )

    return new_filename



# ==========================================================
# Save Uploaded File
# ==========================================================

def save_file(file, upload_folder, allowed_extensions=None):
    """
    Save uploaded file safely.
    """

    if file is None:
        return None


    filename = secure_filename(
        file.filename
    )


    if allowed_extensions:

        if not allowed_file(
            filename,
            allowed_extensions
        ):
            return None


    filename = generate_filename(
        filename
    )


    os.makedirs(
        upload_folder,
        exist_ok=True
    )


    filepath = os.path.join(
        upload_folder,
        filename
    )


    file.save(filepath)


    return filename



# ==========================================================
# Check Allowed File Extension
# ==========================================================

def allowed_file(filename, allowed_extensions):
    """
    Validate file extension.
    """

    return (
        "." in filename
        and
        filename.rsplit(".", 1)[1].lower()
        in allowed_extensions
    )



# ==========================================================
# Date Formatter
# ==========================================================

def format_date(date):

    if date is None:
        return None

    return date.strftime(
        "%d-%m-%Y"
    )



# ==========================================================
# Current Date Time
# ==========================================================

def current_datetime():

    return datetime.now()



# ==========================================================
# Generate API Response
# ==========================================================

def api_response(
        success=True,
        message="",
        data=None,
        status_code=200
):

    return {

        "success": success,

        "message": message,

        "data": data,

        "status": status_code

    }



# ==========================================================
# Pagination Helper
# ==========================================================

def paginate(query, page, per_page=10):

    return query.paginate(

        page=page,

        per_page=per_page,

        error_out=False

    )



# ==========================================================
# Convert Object To Dictionary
# ==========================================================

def object_to_dict(obj):

    result = {}

    for column in obj.__table__.columns:

        result[column.name] = getattr(
            obj,
            column.name
        )

    return result



# ==========================================================
# Search Helper
# ==========================================================

def clean_search_text(text):

    if text is None:
        return ""

    return text.strip().lower()



# ==========================================================
# Generate Random Token
# ==========================================================

def generate_token():

    return str(
        uuid.uuid4()
    )



# ==========================================================
# Delete File
# ==========================================================

def delete_file(filepath):

    if os.path.exists(filepath):

        os.remove(filepath)

        return True

    return False