from flask import Blueprint, render_template, abort
from TSA.routes import staff
home_bp = Blueprint("home", __name__, static_folder="static", template_folder="templates")

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

@home_bp.route("/design-brief")
def design():
    return render_template("design_brief.html")

@home_bp.route('/competition')
def competition():
    return render_template('competition.html')

@home_bp.route('/teachers')
def teachers():
    return render_template('teachers.html', teachers=staff.teachers)

@home_bp.route('/classes')
def classes():
    return render_template('classes.html')

@home_bp.route('/teachers/<string:teacher>')
def staff_member(teacher):
    if not getattr(staff, teacher):
        return abort(404)
    return render_template('teacher.html', teacher=getattr(staff, teacher))
