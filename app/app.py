from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin-pass@localhost/swestaurant_db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def makerequest(item, num):
    # give a fake request to emulate a potential SQL request
    if item == "location":
        return {'id': num, 'imageurl': '../img/austin-tx.jpg', 'address': 'Example', 'neighborhood': 'Example', 'zipcode': '45678-789', 'latitude': 4.5, 'longitude': 4.5, 'restaurant': 1}
    if item == "category":
        return {'id': num, 'name': 'Example', 'restotal': 100, 'reviewtotal': 100, 'ratingavg': 4.5, 'restlist': [1,2,3]}
    if item == "restaurant":
        return {'id': num, 'imageurl': '../img/austin-tx.jpg', 'name': 'Example', 'phonenum': '(123)456-7890', 'rating': 4.5, 'reviewcount': 123, 'url': 'http://google.com', 'location_id': 1, "catlist": [1,2,3]}


@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/location')
def render_location():
    return render_template('location_db.html')
	
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
