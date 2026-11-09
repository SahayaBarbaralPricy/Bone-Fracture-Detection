from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from database.queries import (
    register_user,
    login_user,
    username_exists,
    get_user
)


# ==========================================
# CREATE BLUEPRINT
# ==========================================

auth = Blueprint(
    "auth",
    __name__
)


# ==========================================
# LOGIN
# ==========================================

@auth.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    # ======================================
    # CHECK EXISTING SESSION
    # ======================================

    if "user_id" in session:

        # Verify that the user still exists
        user = get_user(
            session["user_id"]
        )

        if user:

            return redirect(
                url_for("dashboard.home")
            )

        # Old/invalid session
        session.clear()


    # ======================================
    # HANDLE LOGIN FORM
    # ======================================

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )


        # ==================================
        # VALIDATION
        # ==================================

        if not username or not password:

            flash(
                "Please enter username and password.",
                "warning"
            )

            return render_template(
                "login.html"
            )


        # ==================================
        # CHECK DATABASE
        # ==================================

        user = login_user(
            username,
            password
        )


        # ==================================
        # LOGIN SUCCESS
        # ==================================

        if user:

            # Clear any old session data
            session.clear()

            # Store current database user ID
            session["user_id"] = user[0]

            # Store username
            session["username"] = user[4]


            flash(
                "Login Successful!",
                "success"
            )


            return redirect(
                url_for("dashboard.home")
            )


        # ==================================
        # LOGIN FAILED
        # ==================================

        flash(
            "Invalid Username or Password!",
            "danger"
        )


    # ======================================
    # SHOW LOGIN PAGE
    # ======================================

    return render_template(
        "login.html"
    )


# ==========================================
# REGISTER
# ==========================================

@auth.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    # ======================================
    # ALREADY LOGGED IN
    # ======================================

    if "user_id" in session:

        user = get_user(
            session["user_id"]
        )

        if user:

            return redirect(
                url_for("dashboard.home")
            )

        session.clear()


    # ======================================
    # HANDLE REGISTRATION
    # ======================================

    if request.method == "POST":

        fullname = request.form.get(
            "fullname",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )


        # ==================================
        # VALIDATION
        # ==================================

        if (
            not fullname
            or not email
            or not phone
            or not username
            or not password
        ):

            flash(
                "Please fill all fields.",
                "warning"
            )

            return render_template(
                "register.html"
            )


        # ==================================
        # CHECK USERNAME
        # ==================================

        if username_exists(username):

            flash(
                "Username already exists!",
                "warning"
            )

            return render_template(
                "register.html"
            )


        # ==================================
        # REGISTER USER
        # ==================================

        try:

            register_user(
                fullname,
                email,
                phone,
                username,
                password
            )

        except Exception as e:

            flash(
                "Registration failed. Email or username may already exist.",
                "danger"
            )

            return render_template(
                "register.html"
            )


        # ==================================
        # SUCCESS
        # ==================================

        flash(
            "Registration Successful! Please login.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )


    # ======================================
    # SHOW REGISTER PAGE
    # ======================================

    return render_template(
        "register.html"
    )


# ==========================================
# LOGOUT
# ==========================================

@auth.route("/logout")
def logout():

    # Remove all session data
    session.clear()

    flash(
        "Logged Out Successfully!",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )