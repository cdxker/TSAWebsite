from flask import blueprint, render_template

home_bp = blueprint()

@home_bp.route("/")
def hoem():
    return render_template("home.html")