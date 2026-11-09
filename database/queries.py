from database.db import mysql


# ==========================================
# REGISTER USER
# ==========================================

def register_user(
    fullname,
    email,
    phone,
    username,
    password
):

    connection = mysql.connection
    cursor = connection.cursor()

    query = """
        INSERT INTO users
        (
            fullname,
            email,
            phone,
            username,
            password
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            fullname,
            email,
            phone,
            username,
            password
        )
    )

    connection.commit()
    cursor.close()


# ==========================================
# CHECK USERNAME
# ==========================================

def username_exists(username):

    connection = mysql.connection
    cursor = connection.cursor()

    query = """
        SELECT id
        FROM users
        WHERE username = %s
    """

    cursor.execute(
        query,
        (username,)
    )

    user = cursor.fetchone()

    cursor.close()

    return user is not None


# ==========================================
# LOGIN USER
# ==========================================

def login_user(username, password):

    connection = mysql.connection
    cursor = connection.cursor()

    query = """
        SELECT
            id,
            fullname,
            email,
            phone,
            username
        FROM users
        WHERE username = %s
        AND password = %s
    """

    cursor.execute(
        query,
        (
            username,
            password
        )
    )

    user = cursor.fetchone()

    cursor.close()

    return user


# ==========================================
# GET USER
# ==========================================

def get_user(user_id):

    connection = mysql.connection
    cursor = connection.cursor()

    query = """
        SELECT
            id,
            fullname,
            email,
            phone,
            username
        FROM users
        WHERE id = %s
    """

    cursor.execute(
        query,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()

    return user


# ==========================================
# SAVE PREDICTION
# ==========================================

def save_prediction(
    user_id,
    patient_name,
    age,
    gender,
    body_part,
    image_name,
    prediction,
    confidence
):

    connection = mysql.connection
    cursor = connection.cursor()

    query = """
        INSERT INTO predictions
        (
            user_id,
            patient_name,
            age,
            gender,
            body_part,
            image_name,
            prediction_result,
            confidence
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            user_id,
            patient_name,
            age,
            gender,
            body_part,
            image_name,
            prediction,
            confidence
        )
    )

    connection.commit()

    cursor.close()


# ==========================================
# GET USER PREDICTION HISTORY
# ==========================================

def get_prediction_history(user_id):

    connection = mysql.connection
    cursor = connection.cursor()

    query = """
        SELECT
            id,
            user_id,
            patient_name,
            age,
            gender,
            body_part,
            image_name,
            prediction_result,
            confidence,
            report_file,
            predicted_at
        FROM predictions
        WHERE user_id = %s
        ORDER BY predicted_at DESC
    """

    cursor.execute(
        query,
        (user_id,)
    )

    predictions = cursor.fetchall()

    cursor.close()

    return predictions


# ==========================================
# GET SINGLE PREDICTION
# ==========================================

def get_prediction(prediction_id):

    connection = mysql.connection
    cursor = connection.cursor()

    query = """
        SELECT
            id,
            user_id,
            patient_name,
            age,
            gender,
            body_part,
            image_name,
            prediction_result,
            confidence,
            report_file,
            predicted_at
        FROM predictions
        WHERE id = %s
    """

    cursor.execute(
        query,
        (prediction_id,)
    )

    prediction = cursor.fetchone()

    cursor.close()

    return prediction

# ==========================================
# GET USER DETAILS
# ==========================================

def get_user(user_id):

    connection = mysql.connection

    cursor = connection.cursor()

    query = """
        SELECT
            id,
            fullname,
            email,
            phone,
            username
        FROM users
        WHERE id = %s
    """

    cursor.execute(
        query,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()

    return user


# ==========================================
# UPDATE USER DETAILS
# ==========================================

def update_user(
    user_id,
    fullname,
    email,
    phone,
    username
):

    connection = mysql.connection

    cursor = connection.cursor()

    query = """
        UPDATE users
        SET
            fullname = %s,
            email = %s,
            phone = %s,
            username = %s
        WHERE id = %s
    """

    cursor.execute(
        query,
        (
            fullname,
            email,
            phone,
            username,
            user_id
        )
    )

    connection.commit()

    cursor.close()

    return True