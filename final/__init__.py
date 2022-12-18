from flask import Flask
from cs50 import SQL

from final.models import initialize_db
app=Flask(__name__)

app.config["SECRET_KEY"]="thisiscs50project"


db= SQL("sqlite:///database/budgetark.db")
   
from final import routes
