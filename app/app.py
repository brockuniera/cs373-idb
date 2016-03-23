import logging

from flask import Flask, render_template
from flask.ext.script import Manager
from db import db, app

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Welcome to Swestaurants")

manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/location')
def render_location():
    return render_template('location.html')
	
@app.route('/restaurant')
def render_restaurant():
    return render_template('restaurant.html')
	
@app.route('/category')
def render_category():
    return render_template('category.html')
	
@app.route('/about')
def render_about():
    return render_template('about.html')

if __name__ == '__main__':
    manager.run()
