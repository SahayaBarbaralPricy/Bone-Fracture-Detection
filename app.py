from flask import (
    Flask,
    redirect,
    url_for,
    send_from_directory
)

from config import Config
from database.db import init_db

from routes.auth import auth
from routes.dashboard import dashboard
from routes.upload import upload
from routes.prediction import prediction
from routes.history import history
from routes.profile import profile
from routes.report import report


app = Flask(__name__)

app.config.from_object(Config)

init_db(app)

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(upload)
app.register_blueprint(prediction)
app.register_blueprint(history)
app.register_blueprint(profile)
app.register_blueprint(report)


@app.route("/")
def home():
    return redirect(url_for("auth.login"))


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


if __name__ == "__main__":
    app.run(debug=True)