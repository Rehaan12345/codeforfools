from flask import Blueprint, render_template
from flask_login import login_required, current_user

cviews = Blueprint("cviews", __name__)

@cviews.route("/")
def main_home():
    return render_template("mainhome.html", user=current_user, name="main")

@cviews.route("/c/intro")
def intro():
    return render_template("c/intro.html", user=current_user, name="c")

@cviews.route("/c/variables")
def variables():
    return render_template("c/variables.html", user=current_user, name="c")

@cviews.route("/c/operators")
def operators():
    return render_template("c/operators.html", user=current_user, name="c")

@cviews.route("/c/controlflow")
def controlflow():
    return render_template("c/controlflow.html", user=current_user, name="c")

@cviews.route("/c/arrays")
def arrays():
    return render_template("c/arrays.html", user=current_user, name="c")

@cviews.route("/c/pointers")
def pointers():
    return render_template("c/pointers.html", user=current_user, name="c")

@cviews.route("/c/functions")
def functions():
    return render_template("c/functions.html", user=current_user, name="c")

@cviews.route("/c/structures")
def structures():
    return render_template("c/structures.html", user=current_user, name="c")

@cviews.route("/c/files")
def files():
    return render_template("c/files.html", user=current_user, name="c")

@cviews.route("/c/summary")
def summary():
    return render_template("c/summary.html", user=current_user, name="c")