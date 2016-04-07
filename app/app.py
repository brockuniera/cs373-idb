import sys
import unittest
import tests
from io import StringIO
from db import app
from models import Location, Category, Restaurant
import api
from flask import Flask, render_template
from flask.json import dumps
from flask.ext.sqlalchemy import SQLAlchemy

def makerequest(item, num):
    # give a fake request to emulate a potential SQL request
    if item == "location":
        return {'id': num, 'imageurl': '../img/austin-tx.jpg', 'address': str(20), 'neighborhood': 'Example', 'zipcode': '45678-789', 'latitude': 4.5, 'longitude': 4.5, 'restaurant': 1}
    if item == "category":
        return {'id': num, 'name': 'Example', 'resttotal': 100, 'reviewtotal': 100, 'ratingavg': 4.5, 'restlist': [1,2,3]}
    if item == "restaurant":
        return {'id': num, 'imageurl': '../img/austin-tx.jpg', 'name': 'Example', 'phonenum': '(123)456-7890', 'rating': 4.5, 'reviewcount': 123, 'url': 'http://google.com', 'location_id': 1, "catlist": [1,2,3]}

def requestsbyfilter(unknown):
    # if need be
    pass

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/location')
def render_location():

    #return render_template('location_db.html', locAddress = locModel.address)
    # what do we do here, make 10 requests based on incrementing ids
    # then paginate the rest of the requests at the bottom by default?
    #   we have to make a specific routing for filter
    datalist = list();
    datanames = ['id','address','neighborhood','zipcode','latitude','longitude']
    for num in range(1,10):
        datalist.append(makerequest("location",num));
    return render_template('template_db.html',datalist = datalist, datanames = datanames, title = "Locations", datatype = "location")

@app.route('/location/<location_id>')
def render_locatoin_id(location_id=None):
	locdict = makerequest("location",location_id);
	restdict = makerequest("restaurant",locdict['restaurant']);
	return render_template('location.html', locdict = locdict, restdict = restdict)
	
@app.route('/restaurant')
def render_restaurant():
    datalist = list();
    datanames = ['id','name','phonenum','rating','reviewcount']
    for num in range(1,10):
        datalist.append(makerequest("restaurant",num));
    return render_template('template_db.html',datalist = datalist, datanames = datanames, title = "Restaurants", datatype = "restaurant")
	
@app.route('/restaurant/<restaurant_id>')
def render_restaurant_id(restaurant_id=None):
    resdict = makerequest("restaurant",restaurant_id);
    locdict = makerequest("location",resdict['location_id']);
    catlist = list();
    for catnum in resdict['catlist']:
        catlist.append(makerequest("category",catnum));
    return render_template('restaurant.html', restdict = resdict, locdict = locdict, catlist = catlist)

@app.route('/category')
def render_category():
    datalist = list();
    datanames = ['id','name','resttotal','reviewtotal','ratingavg']
    for num in range(1,10):
        datalist.append(makerequest("category",num));
    return render_template('template_db.html',datalist = datalist, datanames = datanames, title = "Categories", datatype = "category")

@app.route('/category/<category_id>')
def render_category_id(category_id=None):
    catdict = makerequest("category",category_id);
    reslist = list();
    for resnum in catdict['restlist']:
        reslist.append(makerequest("restaurant",resnum));
    return render_template('category.html', catdict = catdict, reslist = reslist)

@app.route('/about')
def render_about():
    teststring = str("");
    return render_template('about.html', teststring = teststring)

@app.route('/aboutT')
def render_aboutT():
    test_obj = unittest.TestLoader().loadTestsFromTestCase(tests.tests)
    out_obj = StringIO()
    unittest.TextTestRunner(stream=out_obj).run(test_obj)
    teststring = out_obj.getvalue()
    teststring = teststring.replace('\n', '</br>')
    return render_template('about.html', teststring = teststring)

if __name__ == '__main__':
    api.add_api_routes(app.route)
    app.debug = True
    app.run(host='127.0.0.1') 

