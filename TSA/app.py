from flask import Flask

def create_app():
    from TSA import routes
    app = Flask(__name__)
    routes.init_app(app)
    return app