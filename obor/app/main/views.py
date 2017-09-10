# coding: utf-8
from . import main
from flask import render_template


# test views
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about/')
def about():
    return render_template('about.html')

@main.route('/learn/')
def learn():
    return render_template('learn.html')

@main.route('/login/')
def login():
    return render_template('login.html')

@main.route('/manage/')
def manage():
    return render_template('manage.html')


