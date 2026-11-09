from functools import wraps

from flask import session, redirect, url_for, flash


# ==========================================
# Login Required Decorator
# ==========================================

def login_required(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        # Check whether the user is logged in
        if "user_id" not in session:

            flash(
                "Please login first.",
                "warning"
            )

            return redirect(url_for("auth.login"))

        return view(*args, **kwargs)

    return wrapped_view


# ==========================================
# Get Logged-in User
# ==========================================

def current_user():

    if "user_id" in session:

        return {

            "id": session.get("user_id"),

            "username": session.get("username")

        }

    return None