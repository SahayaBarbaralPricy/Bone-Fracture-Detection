
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "bone_fracture_db")

    UPLOAD_FOLDER = "uploads"

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg"
    }
