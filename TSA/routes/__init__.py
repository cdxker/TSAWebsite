from .home import home_bp
from .pathways import pathway_bp
from .meet the team import meet the team_bp
from flask import Flask

def init_app(app:Flask):
    app.register_blueprint(meet the team_bp)
    app.register_blueprint(pathway_bp)
    app.register_blueprint(home_bp)