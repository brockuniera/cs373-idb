from flask import render_template, Markup, request
from flask.json import dumps
from flask.ext.sqlalchemy import SQLAlchemy
from io import StringIO
import logging
import subprocess
import unittest

import api
from db import app
from models import Location, Category, Restaurant

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
    tableDataDict = getTableDataDict("Locations","location")
    locDataDictList = getDataDictList(getModels(Location, tableDataDict['offset'], 
        tableDataDict['sortby'], tableDataDict['direction']))
    return render_template('template_db.html',
            dataNames=Location.getDataNames(),
            dataList=locDataDictList,
            **tableDataDict
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
    tableDataDict = getTableDataDict("Restaurants","restaurant")
    restDataDictList = getDataDictList(getModels(Restaurant, tableDataDict['offset'], 
        tableDataDict['sortby'], tableDataDict['direction']))
    return render_template('template_db.html',
            dataNames=Restaurant.getDataNames(),
            dataList=restDataDictList,
            **tableDataDict
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
    tableDataDict = getTableDataDict("Categories","category")
    catDataDictList = getDataDictList(getModels(Category, tableDataDict['offset'],
        tableDataDict['sortby'], tableDataDict['direction']))
    return render_template('template_db.html',
            dataNames=Category.getDataNames(),
            dataList=catDataDictList,
            **tableDataDict
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
    teststring = str("");
    return render_template('about.html', teststring = teststring)

@app.route('/aboutT')
def render_aboutT():
    erroutput = subprocess.Popen(['python', 'tests.py'], stderr=subprocess.PIPE).communicate()[1]
    formattedout = "".join(Markup.escape(str(line)) + Markup('<br />') for line in erroutput.decode("utf-8").splitlines())
    return render_template('about.html', teststring=formattedout)

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

def getDirection(direction, changeDir):
    """
    returns the direction that the columns should be sorted
    """
    if direction == None and not changeDir:
        direction = "ascending"
    elif direction == "ascending" and changeDir:
        direction = "descending"
    elif direction == "descending" and changeDir:
        direction = "ascending"
    return direction

def getCaretDir(direction):
    """
    returns the caret direction
    """
    if direction == "ascending":
        return "down"
    return "up"

def getTableDataDict(title, page):
    """
    Common data for table page
    """
    tableDataDict = {}
    changeDir = request.args.get('changedir') and True or False
    tableDataDict['page'] = page
    tableDataDict['title'] = title
    tableDataDict['pagenum'] = request.args.get('page') or 1
    tableDataDict['offset'] = getOffset(tableDataDict['pagenum'])
    tableDataDict['sortby'] = validateSortString(request.args.get('sortby'), Location) or 'id'
    tableDataDict['direction'] = getDirection(request.args.get('dir'), changeDir)
    tableDataDict['caretDir'] = getCaretDir(tableDataDict['direction'])
    return tableDataDict

def getModels(model, offset, sortby, direction):
    """
    Makes query and gets list of models based on it
    """
    query = None;
    if sortby is not None:
        if direction == "ascending":
            modelList = model.query.order_by(
                getattr(model, sortby)).limit(results_per_page).offset(offset)
        else:
            modelList = model.query.order_by(
                    getattr(model, sortby).desc()).limit(results_per_page).offset(offset)
    else:
        modelList = model.query.filter_by().limit(results_per_page).offset(offset)
    return modelList

def getDataDictList(modelList):
    """
    Returns a list of dictionary representations of models based on params
    """
    dataDictList = []
    for modelObj in modelList:
        dataDict = modelObj.__dict__
        dataDict.pop("_sa_instance_state", None) # Weird key added by sqlalchemy
        dataDictList.append(dataDict)
    return dataDictList

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')
