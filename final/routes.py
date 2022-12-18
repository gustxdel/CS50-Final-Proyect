from final import app, db
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from final.forms import RegistrationForm, LoginForm
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash



@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    return render_template("account.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    form=RegistrationForm()
    if form.validate_on_submit():
        username= form.username.data
        password= form.password.data
        confirm= form.confirm_password.data
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) == 1:
            flash(f"Username already in use", category="danger")
            return render_template("register.html",form=form)
        else:
            hashcode = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, password) VALUES(?, ?)", username, hashcode)
        
        flash(f"Account created succesfully", category="success")
        return redirect("/login")
    return render_template("register.html",form=form)
   

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    form=LoginForm()
    if form.validate_on_submit():
        if request.method == "POST":
            username= form.username.data
            password= form.password.data
            rows = db.execute("SELECT * FROM users WHERE username = ?", username)
            hash= check_password_hash(rows[0]["password"])

            if username =="gusifer":
                flash(f"Login unsuccesfully. Incorrect Username or Password", category="danger")    
                return redirect("/login")
            else:
                session["user_id"] = rows[0]["id"]
                flash(f"Login succesfully", category="success")
                return redirect("/account")
    else:    
        return render_template("login.html",form=form)

            


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
   