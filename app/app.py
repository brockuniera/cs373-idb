import logging
from db import app
from models import Location, Category, Restaurant, getDataDictList
from flask import render_template, request
from flask.json import dumps
from flask.ext.sqlalchemy import SQLAlchemy
import api

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# num results we'll display per template_db pages
results_per_page = 25

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def render_location():
    offset = getOffset(request.args.get('page'))
    locDataDictList = getDataDictList(
        Location.query.filter_by().limit(results_per_page).offset(offset))
    return render_template('template_db.html', dataNames = Location.getDataNames(), 
        dataList = dumps(locDataDictList), title = "Locations", page = "location")

@app.route('/location/<location_id>')
def render_locatoin_id(location_id=None):
    locModel = Location.query.get(location_id)
    relatedRestModel = Restaurant.query.filter_by(location_id = location_id).one()
    # TODO get related categories based on the restaurant id
    return render_template('location.html', locModel = locModel, restModel = relatedRestModel)

@app.route('/restaurant')
def render_restaurant():
    offset = getOffset(request.args.get('page'))
    restDataDictList = getDataDictList(
        Restaurant.query.filter_by().limit(results_per_page).offset(offset))
    return render_template('template_db.html', dataNames = Restaurant.getDataNames(), 
        dataList = dumps(restDataDictList), title = "Restaurants", page = "restaurant")

@app.route('/restaurant/<restaurant_id>')
def render_restaurant_id(restaurant_id=None):
    restModel = Restaurant.query.get(restaurant_id)
    relatedLocModel = Location.query.filter_by(id = restModel.location_id).one()
    # TODO get related categories of this restaurant
    return render_template('restaurant.html', restModel = restModel, locModel = relatedLocModel)

@app.route('/category')
def render_category():
    offset = getOffset(request.args.get('page'))
    catDataDictList = getDataDictList(
        Category.query.filter_by().limit(results_per_page).offset(offset))
    return render_template('template_db.html', dataNames = Category.getDataNames(), 
        dataList = dumps(catDataDictList), title = "Categories", page = "category")

@app.route('/category/<category_id>')
def render_category_id(category_id=None):
    catModel = Category.query.get(category_id)
    # TODO get related restaurants of this category
    # TODO get related locations of those restaurants
    return render_template('category.html', catModel = catModel)

@app.route('/about')
def render_about():
    return render_template('about.html')

def getOffset(pagenum):
    if pagenum is not None:
        offset = (int(pagenum)-1) * results_per_page
    else:
        offset = 0
    return offset

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1') 

