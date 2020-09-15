from flask import render_template, flash, redirect
from flask_login import current_user, login_user, logout_user
from .models import User
from .forms import LoginForm, RegisterForm
from . import app, db


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Username or password is incorrect")
            return redirect('/login')

        login_user(user, remember=form.remember_me.data)
        flash("Succesfully signed in!")
        return redirect('/')


    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect('/')

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("User registered for " + form.username.data)
        return redirect('/login')

    return render_template('register.html', form=form)