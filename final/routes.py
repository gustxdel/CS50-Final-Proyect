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
    form=RegistrationForm()
    if form.validate_on_submit():
        username= form.username.data
        password= form.password.data
        confirm= form.confirm_password.data
        hashcode = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username, password) VALUES(?, ?)", username, hashcode)
        
        flash(f"Account created succesfully", category="success")
        return redirect("/login")
    return render_template("register.html",form=form)
   

@app.route("/login", methods=["GET", "POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.username.data=="gusifer" and form.password.data=="12345678":
            flash(f"Login succesfully", category="success")
            return redirect("/account")
        else:
            flash(f"Login unsuccesfully", category="danger")    
    return render_template("login.html",form=form)



   