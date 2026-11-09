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

from model.predict import predict_fracture
from database.queries import save_prediction

import os


# ==========================================
# CREATE BLUEPRINT
# ==========================================

prediction = Blueprint(
    "prediction",
    __name__
)


# ==========================================
# PREDICTION ROUTE
# ==========================================

@prediction.route(
    "/prediction",
    methods=["POST"]
)
def predict():

    # ======================================
    # CHECK LOGIN
    # ======================================

    if "user_id" not in session:

        return redirect(
            url_for("auth.login")
        )


    # ======================================
    # CHECK WHETHER IMAGE EXISTS
    # ======================================

    if "xray_image" not in request.files:

        flash(
            "Please upload an image.",
            "danger"
        )

        return redirect(
            url_for("upload.upload_image")
        )


    file = request.files["xray_image"]


    # ======================================
    # CHECK FILENAME
    # ======================================

    if file.filename == "":

        flash(
            "No image selected.",
            "warning"
        )

        return redirect(
            url_for("upload.upload_image")
        )


    # ======================================
    # GET PATIENT DETAILS
    # ======================================

    patient_name = request.form.get(
        "patient_name",
        ""
    ).strip()

    age = request.form.get(
        "age",
        ""
    ).strip()

    gender = request.form.get(
        "gender",
        ""
    ).strip()

    body_part = request.form.get(
        "body_part",
        ""
    ).strip()


    # ======================================
    # SECURE FILENAME
    # ======================================

    filename = secure_filename(
        file.filename
    )


    # ======================================
    # GET UPLOAD DIRECTORY
    # ======================================

    upload_folder = current_app.config[
        "UPLOAD_FOLDER"
    ]


    # ======================================
    # CREATE DIRECTORY IF NEEDED
    # ======================================

    os.makedirs(
        upload_folder,
        exist_ok=True
    )


    # ======================================
    # CREATE FILE PATH
    # ======================================

    filepath = os.path.join(
        upload_folder,
        filename
    )


    # ======================================
    # SAVE IMAGE
    # ======================================

    file.save(filepath)


    # ======================================
    # CALL AI MODEL
    # ======================================

    try:

        result, confidence = predict_fracture(
            filepath
        )

    except Exception as e:

        flash(
            f"Prediction failed: {str(e)}",
            "danger"
        )

        return redirect(
            url_for("upload.upload_image")
        )


    # ======================================
    # ROUND CONFIDENCE
    # ======================================

    confidence = round(
        float(confidence),
        2
    )


    # ======================================
    # SAVE PREDICTION TO DATABASE
    # ======================================

    save_prediction(

        user_id=session["user_id"],

        patient_name=patient_name,

        age=age,

        gender=gender,

        body_part=body_part,

        image_name=filename,

        prediction=result,

        confidence=confidence

    )


    # ======================================
    # IMAGE URL FOR DISPLAY
    # ======================================

    image_url = url_for(
        "uploaded_file",
        filename=filename
    )


    # ======================================
    # DISPLAY RESULT
    # ======================================

    return render_template(

        "prediction.html",

        image=filename,

        image_url=image_url,

        prediction=result,

        confidence=confidence,

        patient_name=patient_name,

        age=age,

        gender=gender,

        body_part=body_part

    )
