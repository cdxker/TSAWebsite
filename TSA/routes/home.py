from flask import Blueprint, render_template

home_bp = Blueprint("home_bp", __name__, static_folder="static", template_folder="templates")


"""
this adds a route to the /home and / part of the website.
It looks in a similar way as a file system would.
So on /home or slash team the function will return the html needed
"""
@home_bp.route('/')
@home_bp.route("/home")
def home():
    return render_template("home.html")

@home_bp.route("/team")
def team():
    return render_template("meet_the_team.html")
