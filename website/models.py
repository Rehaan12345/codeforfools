from . import db 
from flask_login import UserMixin 

class User(db.Model, UserMixin):
    # Defining a schema, or a layout for some object to be stored in the database:
    id = db.Column(db.Integer, primary_key=True) # This (id) is the primary key, or the unique identifier for every User object created. This unique identifier value is stored as an Integer.
    email = db.Column(db.String(150), unique=True) # Creates a new column for user emails. This will be stored as a String, with the max character limit of 150. Every user must have their own email, meaning the same email cannot be used twice across multiple accounts (will result in an error). 
    username = db.Column(db.String(150)) 
    password = db.Column(db.String(150)) 
    