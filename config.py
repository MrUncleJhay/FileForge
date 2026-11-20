
import os


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-secret-key-change-before-production"
    )

    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB

    UPLOAD_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "uploads"
    )

    ALLOWED_EXTENSIONS = {
        "csv", "xlsx", "xls",
        "pdf", "png", "jpg", "jpeg",
        "gif", "webp", "txt", "json"
    }
