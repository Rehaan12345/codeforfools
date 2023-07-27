from flask import Blueprint, render_template
from flask_login import login_required, current_user

javaviews = Blueprint("javaviews", __name__)

@javaviews.route("/")
def main_home():
    return render_template("mainhome.html", user=current_user, name="main")

@javaviews.route("/java/intro")
def intro():
    return render_template("java/intro.html", user=current_user, name="java")

@javaviews.route("/java/variables")
def variables():
    return render_template("java/variables.html", user=current_user, name="java")

@javaviews.route("/java/operators")
def operators():
    return render_template("java/operators.html", user=current_user, name="java")

@javaviews.route("/java/controlflow")
def controlflow():
    return render_template("java/controlflow.html", user=current_user, name="java")

@javaviews.route("/java/arrays")
def arrays():
    return render_template("java/arrays.html", user=current_user, name="java")

@javaviews.route("/java/oop")
def oop():
    return render_template("java/oop.html", user=current_user, name="java")

@javaviews.route("/java/classes")
def classes():
    return render_template("java/classes.html", user=current_user, name="java")

@javaviews.route("/java/inheritance")
def inheritance():
    return render_template("java/inheritance.html", user=current_user, name="java")

@javaviews.route("/java/exceptions")
def exceptions():
    return render_template("java/exceptions.html", user=current_user, name="java")

@javaviews.route("/java/summary")
def summary():
    return render_template("java/summary.html", user=current_user, name="java")