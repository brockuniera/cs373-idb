import requests
import json
import io

from collections import namedtuple
from db import db
from models import Restaurant, Location, Category
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


"""
Fills all the required key:value data for the restaurant model
"""
def fill_restaurant_data(restaurant, restaurant_data) :
	restaurant_data['name'] = restaurant.name
	restaurant_data['phonenum'] = restaurant.display_phone
	restaurant_data['rating'] = restaurant.rating
	restaurant_data['reviewcount'] = restaurant.review_count
	restaurant_data['url'] = restaurant.url
	restaurant_data['imageurl'] = restaurant.image_url

"""
Fills all the required key:value data for the location model
"""
def fill_location_data(restaurant, location_data):
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

"""
Fills all the required key:value data for the category model
"""
def fill_category_data(restaurant, category_data):
	# category_data is a dict of dicts, ex. {'RestA': {'name': 'RestA',...} ,...}
	for category in restaurant.categories:
		if category.name not in category_data:
			category_data[category.name] = {}
			category_data[category.name]['name'] = category.name
			category_data[category.name]['resttotal'] = 1
			category_data[category.name]['reviewtotal'] = restaurant.review_count
			category_data[category.name]['ratingavg'] = restaurant.rating 
		else:
			category_data[category.name]['resttotal'] += 1
			category_data[category.name]['reviewtotal'] += restaurant.review_count

			# Ratings have to be to the nearest 0.5 to conform to Yelp ratings
			curr_avg = category_data[category.name]['ratingavg']
			category_data[category.name]['ratingavg'] = round(((curr_avg + restaurant.rating)/2) * 2)/2
"""
Retrieves the yelp client authorization, returns the client
"""
def get_yelp_client():
	# Read API key to get access to Yelp API
	with io.open('config_secret.json') as cred:
	    creds = json.load(cred)
	    auth = Oauth1Authenticator(**creds)
	    client = Client(auth)
	return client

def main():
	restaurant_data = {}
	location_data = {}
	category_data = {}
	client = get_yelp_client()

	# Parameters to pass to the Yelp API Search call
	params = {
	    'term': 'restaurants',
	    'lang': 'en',
	    'offset': 2,
	    'limit': 2
	}

    # Remove all current data in the database
    # db.drop_all()
    # db.create_all()

	# Search and phone search responses are parsed into SearchResponse objects.
	while(params['offset'] < 10):
		restaurant_response = client.search('Austin', **params)
		for restaurant in restaurant_response.businesses:

			fill_location_data(restaurant, location_data)
			fill_restaurant_data(restaurant, restaurant_data)
			fill_category_data(restaurant, category_data)

			restModel = Restaurant(**restaurant_data)
			print(restModel)
			# db.session.add(restModel)
			# db.session.commit()

			locModel = Location(**location_data)
			print(locModel)
			# db.session.add(locModel)
			# db.session.commit()

		params['offset'] += 20

	# Add the category data to the database
	for category in category_data:
		catModel = Category(**category_data[category])
		print(catModel)
		# db.session.add(catModel)
		# db.session.commit()

if __name__ == '__main__':
	main()