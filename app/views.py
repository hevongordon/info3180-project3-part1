"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
import os
from flask import session,flash,render_template, request, redirect, url_for
USERNAME="admin"
PASSWORD="naseberry"
SECRET_KEY="super secure key"
from werkzeug import secure_filename


###
# Routing for your application.
###

@app.route('/games', methods=['GET', 'POST'])
def games():
    return render_template('games.html')
     



@app.route('/game/<int:n>')
def game(n):
    if n==1:    
        return render_template("index.html")
    elif n==2:
        return render_template("index2.html")


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
