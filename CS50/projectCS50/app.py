import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

# Make sure API key is set
#if not os.environ.get("API_KEY"):
 #   raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show all goals"""
    user_id = session["user_id"]
    database = db.execute("SELECT * FROM goalsuser WHERE user_id = ? ", user_id)

    return render_template("index.html", database=database)


@app.route("/new", methods=["GET", "POST"])
@login_required
def new():
    """put your new goals"""
    if request.method == "GET":
        return render_template("new.html")
    else:
        symbol = request.form.get("goal")
        if not symbol:
            return apology(" give goal ! ")

        shares = request.form.get("details")

        user_id = session["user_id"]

        db.execute("INSERT INTO goalsuser (user_id, goal, details, state) VALUES (?, ?, ?, ?)",
                   user_id, symbol,  shares, "processing")

        flash("you can do it !!")

        return redirect("/")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("must put own username")
        if not password:
            return apology("must put own password")
        if not confirmation:
            return apology(" confirm password is empty !!")
        if not password == confirmation:
            return apology(" confirm password its not match with your password!")
        hash = generate_password_hash(password)
        try:
            new_user = db.execute("INSERT INTO users (username , hash) VALUES (?, ?)", username, hash)
        except:
            return apology("username already exists")

        session["user_id"] = new_user
        return redirect("/")


@app.route("/done", methods=["GET", "POST"])
@login_required
def done():
    """done goals"""
    if request.method == "GET":
        user_id = session["user_id"]
        symbols = db.execute("SELECT goal FROM goalsuser WHERE user_id = :id GROUP BY goal ", id=user_id)
        return render_template("done.html", symbols=symbols)
    else:
        user_id = session["user_id"]
        goal = request.form.get("goal")

        if not goal:
            return apology(" give symbol ! ")

        db.execute("UPDATE goalsuser SET state = ? WHERE goal = ?", "done", goal)

        flash("done!")

        return redirect("/")
