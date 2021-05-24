"""
The flask application package.
"""

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "asdlkfjlj skldfhj"
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app

