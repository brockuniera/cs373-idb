from flask.json import dumps, jsonify
from models import Category, Restaurant, Location
from db import app

API_ROOT = '/api'
API_URLS = {
    'category_url': '/api/category',
    'location_url': '/api/location',
    'restaurant_url': '/api/restaurant',
}

@app.route('/api')
def api_root():
    "List all of our url end points"
    return jsonify(urls=API_URLS)

# Restaurants

@app.route('/api/restaurant')
def api_list_restaurants():
    "List all of our restaurants"
    dicts = getDataDicts(Restaurant.query.filter_by().all())
    return jsonify(restaurantList=dicts)

@app.route('/api/restaurant/<int:id>')
def api_get_restaurant(id):
    "List a specific restaurant by specifying an id"
    return dumps(getDataDict(Restaurant.query.get(id)))

# Categories

@app.route('/api/category')
def api_list_categories():
    "List all of our categories"
    dicts = getDataDicts(Category.query.filter_by().all())
    return jsonify(categorylist=dicts)

@app.route('/api/category/<int:id>')
def api_get_category(id):
    "List a specific category by specifying an id"
    return dumps(getDataDict(Category.query.get(id)))

# Locations

@app.route('/api/location')
def api_list_locations():
    "List all of our locations"
    dicts = getDataDicts(Location.query.filter_by().all())
    return jsonify(locationlist=dicts)

@app.route('/api/location/<int:id>')
def api_get_location(id):
    "List a specific location by specifying an id"
    return dumps(getDataDict(Location.query.get(id)))

def getDataDicts(modelList):
    """
    Returns a dictionary of dictionaries based on modelList, key is id value is dict
    """
    dataDicts = {}
    for modelObj in modelList:
        dataDicts[modelObj.id] = getDataDict(modelObj)
    return dataDicts

def getDataDict(model):
    """
    Returns a single dictionary of model without sqlalchemy instance key in it
    """
    dataDict = model.__dict__
    dataDict.pop("_sa_instance_state", None)
    return dataDict
