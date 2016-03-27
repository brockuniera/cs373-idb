from flask import Flask, render_template
from db import db, app

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/location')
def render_location():
    return render_template('location_db.html')
	
@app.route('/location/<location_id>')
def render_locatoin_id(location_id=None):
	id = location_id
	return render_template('location.html', id = id)
	
@app.route('/restaurant')
def render_restaurant():
    return render_template('restaurant_db.html')
	
@app.route('/restaurant/<restaurant_id>')
def render_restaurant_id(restaurant_id=None):
	id = restaurant_id
	return render_template('restaurant.html', id = id)
	
@app.route('/category')
def render_category():
    return render_template('category_db.html')
	
@app.route('/category/<category_id>')
def render_category_id(category_id=None):
	id = category_id
	return render_template('category.html', id = id)
	
@app.route('/about')
def render_about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
