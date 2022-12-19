from final import app, db
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from final.forms import RegistrationForm, LoginForm, BudgetForm, ExpensesForm
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash



@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    form=ExpensesForm()
    if request.method=="POST":
        db.execute("INSERT INTO expenses (name, money, userID) VALUES(?, ?, ?)", form.name.data, form.expense.data, session["user_id"])    
        return redirect("/account")
    
    else:
        rows= db.execute("SELECT name, SUM(money) FROM expenses WHERE userID =? GROUP BY name ORDER BY SUM(money) DESC", session["user_id"])
        sum=0
        for row in rows:
            sum += row['SUM(money)']
        
        return render_template("account.html", form=form, sum=sum, rows=rows)

@app.route("/delete", methods=["POST"])
def delete():    
    name = request.form.get("expense_delete")
    db.execute("DELETE from expenses where name=? and userID =?", name, session["user_id"])
    flash(f"Item Deleted succesfully", category="success")
    return redirect("/account")
    
    
@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    form=RegistrationForm()
    if request.method=="POST":
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
    if request.method=="POST":
        
        username=form.username.data
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        user=rows[0]["username"]

        if form.username.data ==user and check_password_hash(rows[0]["password"],form.password.data):
            session["user_id"] = rows[0]["id"]
            flash(f"Login succesfully", category="success")
            return redirect("/account")
        else:
            flash(f"Login unsuccesfully. Incorrect Username or Password", category="danger")    
            return redirect("/login")   
    return render_template("login.html",form=form)

            


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
   