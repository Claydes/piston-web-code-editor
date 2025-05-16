from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import register_views
    register_views(app)

    return app