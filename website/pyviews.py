from flask import Blueprint, render_template
from flask_login import login_required, current_user

pyviews = Blueprint("pyviews", __name__) # A "views" blueprint for the Flask application

@pyviews.route("/")
def main_home():
    return render_template("mainhome.html", user=current_user, name="main")

@pyviews.route("/python") # A decorator -> (The main index page (Home Page))
def home():
    return render_template("/python/intro.html", user=current_user, name="python") # Able to check if this user is authenticated from the home page. 

@pyviews.route("/python/intro") # Introduction to Python Syntax 
def intro():
    return render_template("/python/intro.html", user=current_user, name="python")

@pyviews.route("/python/variables") # Variables and Data Types
def variables():
    return render_template("/python/variables.html", user=current_user, name="python")

@pyviews.route("/python/numeric") # Numeric Data Types
def numeric():
    return render_template("/python/numeric.html", user=current_user, name="python")

@pyviews.route("/python/string") # String Data Types
def string():
    return render_template("/python/string.html", user=current_user, name="python")

@pyviews.route("/python/list") # List Data Type
def list():
    return render_template("/python/list.html", user=current_user, name="python")

@pyviews.route("/python/tuple") # Tuple Data Type
def tuple():
    return render_template("/python/tuple.html", user=current_user, name="python")

@pyviews.route("/python/dictionary") # Dictionary Data Type
def dictionary():
    return render_template("/python/dictionary.html", user=current_user, name="python")

@pyviews.route("/python/set") # Set Data Type
def set():
    return render_template("/python/set.html", user=current_user, name="python")

@pyviews.route("/python/conversion") # Conversion between Data Types
def conversion():
    return render_template("/python/conversion.html", user=current_user, name="python")

@pyviews.route("/python/summary") # Summary and Next Steps
def summary():
    return render_template("/python/summary.html", user=current_user, name="python")