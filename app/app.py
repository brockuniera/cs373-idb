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
    sortby = validateSortString(request.args.get('sortby'), Location)
    direction = validateDirectionString(request.args.get('dir'))

    if sortby is not None:
        if direction == "ascending":
            locDataDictList = getDataDictList(
                Location.query.order_by(getattr(Location, sortby)).all()
            )
        else:
            locDataDictList = getDataDictList(
                Location.query.order_by(getattr(Location, sortby).desc()).all()
            )
    else:
        locDataDictList = Location.query.filter_by().limit(results_per_page).offset(offset)

    return render_template('template_db.html',
            dataNames=Location.getDataNames(),
            dataList=locDataDictList,
            title="Locations",
            page="location",
            direction=direction
        )

@app.route('/location/<location_id>')
def render_location_id(location_id=None):
    locModel = Location.query.get_or_404(location_id)
    relatedRestModel = Restaurant.query.filter_by(location_id = location_id).one()
    catListModels = getDataDictList(relatedRestModel.catlist)
    return render_template('location.html', 
        locModel = locModel, 
        restModel = relatedRestModel,
        catAttrs = Category.getDataNames(),
        catListModels = dumps(catListModels))
# Restaurant

@app.route('/restaurant')
def render_restaurant():
    # Get query string args
    offset = getOffset(request.args.get('page'))
    sortby = validateSortString(request.args.get('sortby'), Restaurant)
    direction = validateDirectionString(request.args.get('dir'))

    if sortby is not None:
        if direction == "ascending":
            restDataDictList = getDataDictList(
                Restaurant.query.order_by(getattr(Restaurant, sortby)).all()
            )
        else:
            restDataDictList = getDataDictList(
                Restaurant.query.order_by(getattr(Restaurant, sortby).desc()).all()
            )
    else:
        restDataDictList = Restaurant.query.filter_by().limit(results_per_page).offset(offset)

    return render_template('template_db.html',
            dataNames=Restaurant.getDataNames(),
            dataList=restDataDictList,
            title="Restaurants",
            page="restaurant",
            direction=direction
        )

@app.route('/restaurant/<restaurant_id>')
def render_restaurant_id(restaurant_id=None):
    restModel = Restaurant.query.get_or_404(restaurant_id)
    relatedLocModel = Location.query.get(restModel.location_id)
    catListModels = getDataDictList(restModel.catlist)
    return render_template('restaurant.html', 
        restModel = restModel, 
        locModel = relatedLocModel,
        catAttrs = Category.getDataNames(),
        catListModels = dumps(catListModels))

# Category

@app.route('/category')
def render_category():
    # Get query string args
    offset = getOffset(request.args.get('page'))
    sortby = validateSortString(request.args.get('sortby'), Category)
    direction = validateDirectionString(request.args.get('dir'))

    if sortby is not None:
        if direction == "ascending":
            catDataDictList = getDataDictList(
                Category.query.order_by(getattr(Category, sortby)).all()
            )
        else:
            catDataDictList = getDataDictList(
                Category.query.order_by(getattr(Category, sortby).desc()).all()
            )
    else:
        catDataDictList = Category.query.filter_by().limit(results_per_page).offset(offset)

    return render_template('template_db.html',
            dataNames=Category.getDataNames(),
            dataList=catDataDictList,
            title="Categories",
            page="category",
            direction=direction
        )

@app.route('/category/<category_id>')
def render_category_id(category_id=None):
    imgList = list()
    imgIndex = 1
    catModel = Category.query.get_or_404(category_id)
    for restModel in catModel.restlist:
        if(imgIndex <= 5):
            imgList.append((imgIndex, restModel.imageurl))

    relatedRestModels = getDataDictList(catModel.restlist)
    return render_template('category.html', 
        catModel = catModel, 
        restAttrs = Restaurant.getDataNames(),
        imgList = imgList,
        restListModels = dumps(relatedRestModels))

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
    except (ValueError, TypeError):
        pass
    return offset

def validateSortString(sortstring, classmodel):
    """
    Given a sortstring and the class of the model (ie: Restaurant, Category, Location)
    classmodel needs a getDataNames() static method
    return None if sortstring is not a (sortable?) attribute in classmodel
    """
    return sortstring if sortstring in classmodel.getDataNames() else None

def validateDirectionString(querydirection):
    direction = querydirection or "ascending"
    if direction == "ascending":
        direction = "descending"
    else:
        direction = "ascending"
    return direction


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')
