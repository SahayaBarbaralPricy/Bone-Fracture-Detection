from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app,
    session
)

from werkzeug.utils import secure_filename

import os


# ==========================================
# CREATE BLUEPRINT
# ==========================================

upload = Blueprint(
    "upload",
    __name__
)


# ==========================================
# ALLOWED FILE EXTENSIONS
# ==========================================

def allowed_file(filename):

    allowed_extensions = current_app.config[
        "ALLOWED_EXTENSIONS"
    ]

    return (
        "." in filename
        and
        filename.rsplit(".", 1)[1].lower()
        in allowed_extensions
    )


# ==========================================
# UPLOAD PAGE
# ==========================================

@upload.route(
    "/upload",
    methods=["GET", "POST"]
)
def upload_image():

    # ======================================
    # AUTHENTICATION CHECK
    # ======================================

    if "user_id" not in session:

        flash(
            "Please login first.",
            "warning"
        )

        return redirect(
            url_for("auth.login")
        )


    # ======================================
    # POST REQUEST
    # ======================================

    if request.method == "POST":

        # -------------------------------
        # CHECK FILE
        # -------------------------------

        if "xray_image" not in request.files:

            flash(
                "Please select an image.",
                "danger"
            )

            return redirect(request.url)


        file = request.files["xray_image"]


        # -------------------------------
        # CHECK FILENAME
        # -------------------------------

        if file.filename == "":

            flash(
                "No file selected.",
                "warning"
            )

            return redirect(request.url)


        # -------------------------------
        # VALIDATE FILE
        # -------------------------------

        if not allowed_file(file.filename):

            flash(
                "Only PNG, JPG and JPEG files are allowed.",
                "danger"
            )

            return redirect(request.url)


        # -------------------------------
        # SECURE FILENAME
        # -------------------------------

        filename = secure_filename(
            file.filename
        )


        # -------------------------------
        # UPLOAD DIRECTORY
        # -------------------------------

        upload_folder = current_app.config[
            "UPLOAD_FOLDER"
        ]


        # -------------------------------
        # CREATE DIRECTORY
        # -------------------------------

        os.makedirs(
            upload_folder,
            exist_ok=True
        )


        # -------------------------------
        # FILE PATH
        # -------------------------------

        filepath = os.path.join(
            upload_folder,
            filename
        )


        # -------------------------------
        # SAVE IMAGE
        # -------------------------------

        file.save(filepath)


        flash(
            "Image uploaded successfully!",
            "success"
        )


        return redirect(
            url_for("upload.upload_image")
        )


    # ======================================
    # DISPLAY UPLOAD PAGE
    # ======================================

    return render_template(
        "upload.html"
    )