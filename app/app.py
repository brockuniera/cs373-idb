import api
import logging

from db import app
from models import Location, Category, Restaurant, getDataDictList
from flask import Flask, render_template
from flask.json import dumps
from flask.ext.sqlalchemy import SQLAlchemy

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def render_location():
    locDataDictList = getDataDictList(Location.query.filter_by().all())
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
    restDataDictList = getDataDictList(Restaurant.query.filter_by().all())
    return render_template('template_db.html', dataNames = Restaurant.getDataNames(), 
        dataList = dumps(restDataDictList), title = "Restaurants", page = "restaurant")

@app.route('/restaurant/<restaurant_id>')
def render_restaurant_id(restaurant_id=None):
    restModel = Restaurant.query.get(restaurant_id)
    relatedLocModel = Location.query.filter_by(location_id = restModel.location_id).one()
    return render_template('restaurant.html', restModel = restModel, locModel = relatedLocModel)

@app.route('/category')
def render_category():
    catDataDictList = getDataDictList(Category.query.filter_by().all())
    logger.debug(catDataDictList[0])
    return render_template('template_db.html', dataNames = Category.getDataNames(), 
        dataList = dumps(catDataDictList), title = "Categories", page = "category")
    return render_template('template_db.html')

@app.route('/category/<category_id>')
def render_category_id(category_id=None):
    return render_template('category.html')

@app.route('/about')
def render_about():
    return render_template('about.html')

if __name__ == '__main__':
    api.add_api_routes(app.route)
    app.debug = True
    app.run(host='127.0.0.1') 

