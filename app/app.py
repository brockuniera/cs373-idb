import os

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def makerequest(item, num):
    # give a fake request to emulate a potential SQL request
    if item == "location":
        return {'id': num, 'imageurl': '../img/austin-tx.jpg', 'address': 'Example', 'neighborhood': 'Example', 'zipcode': '45678-789', 'latitude': 30.2849, 'longitude': -97.7341, 'restaurant': 1}
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
    return render_template('location_db.html', locAddress = locModel.address)
	
@app.route('/location/<location_id>')
def render_locatoin_id(location_id=None):
	locdict = makerequest("location",location_id);
	restdict = makerequest("restaurant",locdict['restaurant']);
	return render_template('location.html', locdict = locdict, restdict = restdict)
	
@app.route('/restaurant')
def render_restaurant():
    return render_template('restaurant_db.html')
	
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
    return render_template('category_db.html')

@app.route('/category/<category_id>')
def render_category_id(category_id=None):
    catdict = makerequest("category",category_id);
    reslist = list();
    for resnum in catdict['restlist']:
        reslist.append(makerequest("restaurant",resnum));
    return render_template('category.html', catdict = catdict, reslist = reslist)

@app.route('/about')
def render_about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
