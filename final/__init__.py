from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SECRET_KEY"]="thisiscs50project"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database/budgetark.db"

db = SQLAlchemy(app)

from final import routes
