from flask import Blueprint, render_template, session, redirect, url_for

# Create Blueprint
dashboard = Blueprint("dashboard", __name__)


# ==========================================
# Dashboard
# ==========================================
@dashboard.route("/dashboard")
def home():

    # Check whether the user is logged in
    if "user_id" not in session:

        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        username=session.get("username")
    )