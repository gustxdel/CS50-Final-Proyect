from flask import Flask
from cs50 import SQL
from flask_session import Session
from tempfile import mkdtemp


app=Flask(__name__)

app.config["SECRET_KEY"]="thisiscs50project"
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db= SQL("sqlite:///final/database/budgetark.db")
   
from final import routes
