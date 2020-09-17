from flask import render_template, flash, redirect, abort
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Event
from .forms import LoginForm, RegisterForm, EventForm
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


@app.route('/calender')
@login_required
def calender():

    events = Event.query.all()
    events = reversed(events)

    return render_template("calender.html", events=events)


@app.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():

    form = EventForm()
    if form.validate_on_submit():
        event_name = form.event_name.data
        event_date = form.event_date.data # This returns a date as a python datetime.date object yyyy-mm-dd
        event_description = form.event_description.data

        new_event = Event(event_name=event_name, event_date=event_date, event_description=event_description, user_id=current_user.id)
        db.session.add(new_event)
        db.session.commit()

        flash(f"Created event '{event_name}'!")
        return redirect('/calender')

    return render_template("create_event.html", form=form)


@app.route('/users/<username>')
def user_page(username):

    user = User.query.filter_by(username=username).first()

    if user:
        events = user.events
        return render_template("user_page.html", username=username, events=events)

    else:
        abort(404)

    return
