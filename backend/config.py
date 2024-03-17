from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # Cross Origin Request , send from a differfent URL, not from the same server

app = Flask(__name__)

CORS(app) # Wrap the app in CORS, to send cross origin requests (from another server)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" # Set the Database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Not track all the modifications made to database

db = SQLAlchemy(app) # Make an instance of the database that we specified above


