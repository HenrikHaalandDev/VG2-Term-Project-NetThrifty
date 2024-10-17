from flask import Flask, render_template, url_for, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
import my_secrets
import pymysql
from datetime import datetime

# Define the path to the templates directory
template_dir = os.path.abspath('../frontend/templates')

# Set up the connection to the database
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
    my_secrets.dbuser, my_secrets.dbpass, my_secrets.dbhost, my_secrets.dbname 
)


app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
print("Connection to database:", app.config['SQLALCHEMY_DATABASE_URI'])

# Initialize SQLAlchemy
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html') 

