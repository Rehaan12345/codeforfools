from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash 
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import git

auth = Blueprint("auth", __name__) # An "auth" blueprint for the Flask application

@auth.route("/git_update", methods=["POST"])
def git_update():
    repo = git.Repo("./codeforfools")  
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "", 200

@auth.route("/login", methods=["GET", "POST"]) 
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first() # Filters all of the users who have this email.
        if user: # If this user is found: 
            if check_password_hash(user.password, password): # Checks this user's password.
                flash("Successfully logged in", category="success")
                login_user(user, remember=True) # Logs in the user. Remembers the fact that this user is logged in until the user clears their browser history / session. Will be stored in the flask webserver - until the webserver restarts. 
                return render_template("mainhome.html", user=current_user, name="main")
            else:
                flash("Incorrect password, try again!", category="error")
        else: # If this user is not found:
            flash("This email does not belong to an account. Try creating a new account!", category="error")

    return render_template("login.html", user=current_user, name="auth")

@auth.route("/logout") 
@login_required # Makes sure we cannot access this route / page unless the user is logged in - can't logged out if not logged in.  
def logout():
    logout_user() # Logs out the current user. 
    return redirect(url_for("auth.login"))

@auth.route("/signup", methods=["GET", "POST"]) 
def signup(): 
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password") 

        # Makes sure two users don't use the same email address: 
        user = User.query.filter_by(email=email).first() 
        if user: 
            flash("This email is already linked to an account!", category="error") 
        elif len(email) < 4: 
            flash("Your email must be greater than 3 characters!", category="error")
        elif len(username) < 2:
            flash("Your username must have more than 1 character!", category="error") 
        elif password != confirm_password:
            flash("Your passwords do not match!", category="error") 
        elif len(password) < 7:
            flash("Your password must be greater than 6 characters!", category="error")
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user) 
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Your account has been created!", category="success")
            return render_template("mainhome.html", user=current_user, name="main")

    return render_template("signup.html", user=current_user, name="auth")