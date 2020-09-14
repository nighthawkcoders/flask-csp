from flask import render_template, flash
from . import app, db


@app.route('/')
def home():
    return "home page"