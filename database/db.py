from flask_mysqldb import MySQL

mysql = MySQL()


def init_db(app):

    mysql.init_app(app)

    with app.app_context():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT DATABASE();")

            database = cursor.fetchone()

            print("===================================")
            print("✅ MySQL Connected Successfully")
            print("Current Database :", database)
            print("===================================")

            cursor.close()

        except Exception as e:
            print("===================================")
            print("❌ MySQL Connection Failed")
            print(e)
            print("===================================")