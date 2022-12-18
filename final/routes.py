from final import app
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from final.forms import RegistrationForm, LoginForm
from flask_session import Session
from final.models import User


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
        user=User(username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
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



   