from .home import home_bp
from .pathway import pathway_bp
from flask import Flask

def init_app(app:Flask):
    # This connects all the smaller blueprints together to merch it with the app
    app.register_blueprint(pathway_bp)
    app.register_blueprint(home_bp)