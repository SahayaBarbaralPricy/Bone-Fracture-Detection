from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session
)

from database.queries import get_prediction_history


# ==========================================
# CREATE BLUEPRINT
# ==========================================

history = Blueprint(
    "history",
    __name__
)


# ==========================================
# PREDICTION HISTORY
# ==========================================

@history.route("/history")
def prediction_history():

    # ======================================
    # CHECK LOGIN
    # ======================================

    if "user_id" not in session:

        return redirect(
            url_for("auth.login")
        )


    # ======================================
    # GET LOGGED-IN USER ID
    # ======================================

    user_id = session["user_id"]


    # ======================================
    # GET USER HISTORY
    # ======================================

    predictions = get_prediction_history(
        user_id
    )


    # ======================================
    # DISPLAY HISTORY
    # ======================================

    return render_template(
        "history.html",
        predictions=predictions
    )