from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
DB_NAME = "database.db"

admin = Admin()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "rehaan" 
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"  
    db.init_app(app) 

    # Importing the blueprints:
    from .pyviews import pyviews
    from .auth import auth 
    from .cviews import cviews 
    from .javaviews import javaviews 

    # Registering the blueprints with the Flask application:
    app.register_blueprint(pyviews, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(cviews, url_prefix="/")
    app.register_blueprint(javaviews, url_prefix="/")
    
    # Import the User class
    from .models import User 

    with app.app_context():
        db.create_all()
        admin.init_app(app)

    admin.add_view(ModelView(User, db.session))

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" # Where the user goes if they're not logged in. 
    login_manager.init_app(app) # Tells the login manager which app is currently being used. 

    @login_manager.user_loader 
    def load_user(id): 
        return User.query.get(int(id)) # Tells flask how to load the user. By default, it looks for the primary key (id). 

    return app 
