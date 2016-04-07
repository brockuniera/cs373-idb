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

#
# Views
#

@app.route('/')
def index():
    return render_template('index.html')

# Location

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
    return render_template('location.html', locModel = locModel, restModel = relatedRestModel)

# Restaurant

@app.route('/restaurant')
def render_restaurant():
    # Get query string args
    offset = getOffset(request.args.get('page'))
    sortby = validateSortString(request.args.get('sortby'))

    restDataDictList = getDataDictList(
        Restaurant.query.filter_by().limit(results_per_page).offset(offset).order_by(sortby and getattr(Restaurant, sortby))
    )

    return render_template('template_db.html',
            dataNames=Restaurant.getDataNames(),
            dataList=dumps(restDataDictList),
            title="Restaurants",
            page="restaurant"
        )

@app.route('/restaurant/<restaurant_id>')
def render_restaurant_id(restaurant_id=None):
    restModel = Restaurant.query.get_or_404(restaurant_id)
    relatedLocModel = Location(id = restModel.location_id).one()
    # TODO get related categories of this restaurant
    return render_template('restaurant.html', restModel = restModel, locModel = relatedLocModel)

# Category

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
    locModelList = list()
    imgList = list()
    imgIndex = 1
    for restModel in catModel.restlist:
        if(imgIndex <= 5):
            imgList.append((imgIndex, restModel.imageurl))
        locModelList.append(Location.query.get(restModel.location_id))
    return render_template('category.html', catModel = catModel, locModelList = locModelList,
        imgList = imgList)

@app.route('/about')
def render_about():
    return render_template('about.html')

#
# Helper functions
#

def getOffset(pagenumstr):
    """
    Given a pagenum string from a query string,
    return the offset into the results
    """
    offset = 0
    try:
        offset = (int(pagenumstr) - 1) * results_per_page
    except ValueError:
        pass
    return offset

def validateSortString(sortstring, classmodel):
    """
    Given a sortstring and the class of the model (ie: Restaurant, Category, Location)
    classmodel needs a getDataNames() static method
    return None if sortstring is not a (sortable?) attribute in classmodel
    """
    return sortstring if sortstring in classmodel.getDataNames() else None

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')
