from flask import Flask
from flask.json import dumps, jsonify
from models import Category, Restaurant, Location

API_ROOT = '/api'
API_URLS = {
    'category_url': '/api/category',
    'location_url': '/api/location',
    'restaurant_url': '/api/restaurant',
}

def add_api_routes(route):
    @route('/api')
    def api_root():
        "List all of our url end points"
        return jsonify(urls=API_URLS)

    # Restaurants

    @route('/api/restaurant')
    def api_list_restaurants():
        "List all of our restaurants"
        return jsonify(restaurantlist={i.id : i.__dict__ for i in Restaurant.query.all()})

    @route('/api/restaurant/<int:id>')
    def api_get_restaurant(id):
        "List a specific restaurant by specifying an id"
        return dumps(Restaurant.query.get(id).__dict__)

    @route('/api/restaurant?q=<filterstring>')
    def api_filter_restaurants(filterstring):
        "List a specific restaurant by specifying an id"
        # TODO Parse filterstring and cop some info
        return dumps(Restaurant.query.filter_by(name="TODO parse the filterstring").__dict__)

    # Categories

    @route('/api/category')
    def api_list_categories():
        "List all of our categories"
        return jsonify(categorylist={i.id : i.__dict__ for i in Category.query.all()})

    @route('/api/category/<int:id>')
    def api_get_category(id):
        "List a specific category by specifying an id"
        return dumps(Category.query.get(id).__dict__)

    @route('/api/category?q=<filterstring>')
    def api_filter_categories(filterstring):
        "List a specific category by specifying an id"
        # TODO Parse filterstring and cop some info
        return dumps(Category.query.filter_by(name="TODO parse the filterstring").__dict__)

    # Locations

    @route('/api/location')
    def api_list_locations():
        "List all of our locations"
        return jsonify(locationlist={i.id : i.__dict__ for i in Location.query.all()})

    @route('/api/location/<int:id>')
    def api_get_location(id):
        "List a specific location by specifying an id"
        return dumps(Location.query.get(id).__dict__)

    @route('/api/location?q=<filterstring>')
    def api_filter_locations(filterstring):
        "List a specific location by specifying an id"
        # TODO Parse filterstring and cop some info
        return dumps(Location.query.filter_by(name="TODO parse the filterstring").__dict__)
