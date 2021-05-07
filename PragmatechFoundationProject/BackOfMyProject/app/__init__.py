from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# admin routes

from admin.routes import *

# main routes

from main.routes import *
