import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secret-key-goes-here-123-456-789-0"
    TEMPLATES_AUTO_RELOAD = True
    UPLOAD_FOLDER = os.path.join(basedir, "app", "static", "uploads")
