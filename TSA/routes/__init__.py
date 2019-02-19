from .home import home_bp
from .pathways import pathway
from flask import Flask

def init_app(app:Flask):
    app.register_blueprint(home_bp)