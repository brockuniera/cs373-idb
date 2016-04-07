import requests
import json
import io
import re

from db import app, db
from flask.ext.script import Manager
from models import Restaurant, Location, Category
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

manager = Manager(app)

def fill_restaurant_data(restaurant, restaurant_data) :
    """
    Fills all the required key:value data for the restaurant model
    """
    restaurant_data['name'] = restaurant.name
    restaurant_data['phonenum'] = restaurant.display_phone
    restaurant_data['rating'] = restaurant.rating
    restaurant_data['reviewcount'] = restaurant.review_count
    restaurant_data['url'] = restaurant.url 
    restaurant_data['imageurl'] = re.sub(r'\/\w+\.jpg', r'/ls.jpg', restaurant.image_url)

def fill_location_data(restaurant, location_data):
    """
    Fills all the required key:value data for the location model
    """
    # Not all locations have a neighborhood (e.g. the airport restaurants)
    if(restaurant.location.neighborhoods != None):
        location_data['neighborhood'] = restaurant.location.neighborhoods[0]
    else:
        location_data['neighborhood'] = "None"

    # Address is returned as a list
    address = str()
    for addr in restaurant.location.address:
            address += addr

    location_data['address'] = address
    location_data['zipcode'] = restaurant.location.postal_code
    location_data['latitude'] = restaurant.location.coordinate.latitude
    location_data['longitude'] = restaurant.location.coordinate.longitude

def fill_category_data(restaurant, restModel, category_data):
    """
    Fills all the required key:value data for the category model
    """
    # category_data is a dict of (RestaurantName : RestaurantDict), ex. {'RestA': {'name': 'RestA',...} ,...}
    for category in restaurant.categories:
        catname = category.name
        if catname not in category_data:
            # Create the dictionary for this category
            # This is where all categories get created
            catdict = {}
            catdict['name'] = catname
            catdict['resttotal'] = 1
            catdict['reviewtotal'] = restaurant.review_count
            catdict['ratingavg'] = restaurant.rating
            catdict['restlist'] = [restModel]

            # Add the catdict to category_data dict
            category_data[catname] = catdict
        else:
            # Get the category
            catdict = category_data[catname]

            # Update counters...
            catdict['resttotal'] += 1
            catdict['reviewtotal'] += restaurant.review_count

            # ...add this restaurant to this catdicts list of restaurants...
            catdict['restlist'].append(restModel)

            # ...ratings have to be to the nearest 0.5 to conform to Yelp ratings
            curr_avg = catdict['ratingavg']
            catdict['ratingavg'] = round(((curr_avg + restaurant.rating)/2) * 2)/2

def get_yelp_client():
    """
    Retrieves the yelp client authorization, returns the client
    """
    # Read API key to get access to Yelp API
    with io.open('config_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)
    return client

@manager.command
def create_db():
    restaurant_data = {}
    location_data = {}
    category_data = {}
    catname_to_restlist = {}
    client = get_yelp_client()

    # Parameters to pass to the Yelp API Search call
    params = {
        'term': 'restaurants',
        'lang': 'en',
        'offset': 1,
        'limit': 20, # Max is 20
    }
    offset_limit = 40

    # Remove all current data in the database
    # db.drop_all()
    db.create_all()

    # Search and phone search responses are parsed into SearchResponse objects.
    while(params['offset'] < offset_limit):
        restaurant_response = client.search('Austin', **params)
        for restaurant in restaurant_response.businesses:
            fill_location_data(restaurant, location_data)
            fill_restaurant_data(restaurant, restaurant_data)

            # Build restModel and pass to fill_category_data
            restModel = Restaurant(**restaurant_data)
            fill_category_data(restaurant, restModel, category_data)

            locModel = Location(**location_data)

            # Adding the relationship
            restModel.location = locModel

            db.session.add(restModel)
            db.session.commit()
            db.session.add(locModel)
            db.session.commit()

        params['offset'] += 20

    # Add the category data to the database
    for category in category_data:
        catModel = Category(**category_data[category])
        #print("Categoryname: '{}', List:'{}'".format(catModel.name, [i.name for i in catModel.restlist]))
        db.session.add(catModel)
        db.session.commit()

if __name__ == '__main__':
    manager.run()
