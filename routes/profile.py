from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from database.queries import (
    get_user,
    update_user
)

# ==========================================
# Blueprint
# ==========================================

profile = Blueprint("profile", __name__)


# ==========================================
# View & Update Profile
# ==========================================

@profile.route("/profile", methods=["GET", "POST"])
def user_profile():

    # User must be logged in
    if "user_id" not in session:

        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    # -----------------------------
    # Update Profile
    # -----------------------------
    if request.method == "POST":

        fullname = request.form.get("fullname")
        email = request.form.get("email")
        phone = request.form.get("phone")

        update_user(
            user_id,
            fullname,
            email,
            phone
        )

        flash(
            "Profile updated successfully!",
            "success"
        )

        return redirect(url_for("profile.user_profile"))

    # -----------------------------
    # Display Profile
    # -----------------------------
    user = get_user(user_id)

    return render_template(
        "profile.html",
        user=user
    )