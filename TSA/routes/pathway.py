from flask import Blueprint, render_template

pathway_bp = Blueprint("pathways_bp", __name__, static_folder="static", template_folder="templates")

# Adds a new route onto the /pathways
@pathway_bp.route("/pathways")
def pathways():
    return render_template("pathways.html")
