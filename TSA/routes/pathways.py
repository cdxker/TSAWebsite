from flask import Blueprint, render_template

home_bp = Blueprint("pathways_bp", __name__, static_folder="static", template_folder="templates")

@home_bp.route("/")
def hoem():
    return render_template("pathways.html")
