from flask import Flask

# New imports
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ

# not needed for SQLite3
# import mysql.connector

# force loading of environment variables
load_dotenv('.flaskenv')

# Get the environment variables from .flaskenv
#IP = environ.get('MYSQL_IP')
#USERNAME = environ.get('MYSQL_USER')
#PASSWORD = environ.get('MYSQL_PASS')

DB_NAME = environ.get('SQLITE_DB')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csc33O'

# Specify the connection parameters/credentials for the database
# DB_CONFIG_STR = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{IP}/{DB_NAME}"
DB_CONFIG_STR = 'sqlite:///' + DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG_STR
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

# Create database connection and associate it with the Flask application
db = SQLAlchemy(app)

# Add models
from app import routes, models
