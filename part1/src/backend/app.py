from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import my_secrets
import pymysql
from datetime import datetime


# Connection to database 
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
    my_secrets.dbuser, my_secrets.dbpass, my_secrets.dbhost, my_secrets.dbname 
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
print("Connection to database:", app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)


