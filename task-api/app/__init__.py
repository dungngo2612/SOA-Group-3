"""Create and configure the Flask application."""

from flask import Flask

from .routes import books_bp


def create_app(test_config=None):
    """Application factory used by the server and tests."""
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(books_bp)
    return app
