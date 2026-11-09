from flask import (
    Blueprint,
    render_template,
    send_file,
    flash,
    redirect,
    url_for,
    session
)

import os

from database.queries import (
    get_prediction_history,
    get_prediction
)

from reports.report_generator import generate_report


# ==========================================
# CREATE BLUEPRINT
# ==========================================

report = Blueprint(
    "report",
    __name__
)


# ==========================================
# REPORTS PAGE
# ==========================================

@report.route("/reports")
def reports():

    # ======================================
    # CHECK LOGIN
    # ======================================

    if "user_id" not in session:

        return redirect(
            url_for("auth.login")
        )


    # ======================================
    # GET LOGGED-IN USER
    # ======================================

    user_id = session["user_id"]


    # ======================================
    # GET USER PREDICTIONS
    # ======================================

    predictions = get_prediction_history(
        user_id
    )


    # ======================================
    # DISPLAY REPORTS PAGE
    # ======================================

    return render_template(
        "reports.html",
        predictions=predictions
    )


# ==========================================
# GENERATE AND DOWNLOAD REPORT
# ==========================================

@report.route(
    "/report/download/<int:prediction_id>"
)
def download_report(prediction_id):

    # ======================================
    # CHECK LOGIN
    # ======================================

    if "user_id" not in session:

        return redirect(
            url_for("auth.login")
        )


    # ======================================
    # GET PREDICTION
    # ======================================

    prediction = get_prediction(
        prediction_id
    )


    # ======================================
    # CHECK PREDICTION EXISTS
    # ======================================

    if not prediction:

        flash(
            "Prediction not found.",
            "danger"
        )

        return redirect(
            url_for("report.reports")
        )


    # ======================================
    # SECURITY CHECK
    # ======================================

    if prediction[1] != session["user_id"]:

        flash(
            "You are not authorized to download this report.",
            "danger"
        )

        return redirect(
            url_for("report.reports")
        )


    # ======================================
    # GET PREDICTION DATA
    # ======================================

    patient_name = prediction[2] or "Not Provided"

    age = prediction[3] or "Not Provided"

    gender = prediction[4] or "Not Provided"

    body_part = prediction[5] or "Not Provided"

    image_name = prediction[6]

    prediction_result = prediction[7]

    confidence = prediction[8]

    predicted_at = prediction[10]


    # ======================================
    # GET UPLOADED IMAGE PATH
    # ======================================

    upload_folder = os.path.abspath(
        os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "uploads"
        )
    )

    image_path = os.path.join(
        upload_folder,
        image_name
    )


    # ======================================
    # CHECK IMAGE EXISTS
    # ======================================

    if not os.path.exists(image_path):

        image_path = None


    # ======================================
    # CREATE PDF FILENAME
    # ======================================

    filename = (
        f"report_{prediction_id}.pdf"
    )


    # ======================================
    # GENERATE PDF
    # ======================================

    pdf_path = generate_report(

        filename=filename,

        patient_name=patient_name,

        age=age,

        gender=gender,

        body_part=body_part,

        prediction=prediction_result,

        confidence=confidence,

        image_path=image_path,

        predicted_at=predicted_at
    )


    # ======================================
    # CHECK PDF EXISTS
    # ======================================

    if not pdf_path or not os.path.exists(pdf_path):

        flash(
            "Unable to generate report.",
            "danger"
        )

        return redirect(
            url_for("report.reports")
        )


    # ======================================
    # DOWNLOAD PDF
    # ======================================

    return send_file(

        pdf_path,

        as_attachment=True,

        download_name=filename,

        mimetype="application/pdf"
    )