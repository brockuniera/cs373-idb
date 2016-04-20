import os
import logging
import time

from whoosh import index, qparser
from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED
from whoosh.qparser import MultifieldParser
from models import Restaurant, Location, Category

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

whoosh_index_path = "whoosh_index"

def create_whoosh_dir():
    if not os.path.exists(whoosh_index_path):
        os.mkdir(whoosh_index_path)

# Restaurant Schema and Index

class RestaurantSchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True)
    phonenum = KEYWORD(stored=True)
    rating = ID(stored=True)
    reviewcount = ID(stored=True)

def get_restaurant_index():
    if(index.exists_in(whoosh_index_path, indexname="restaurant_index")):
        rest_ix = index.open_dir(whoosh_index_path, indexname="restaurant_index")
    else:
        rest_ix = index.create_in(whoosh_index_path, schema=RestaurantSchema(), 
            indexname="restaurant_index")
        fill_restaurant_index(rest_ix)
    return rest_ix
    
def fill_restaurant_index(ix):
    writer = ix.writer()

    restModelList = Restaurant.query.filter_by().all()
    for restModel in restModelList:
        writer.add_document(name=restModel.name, 
            id=str(restModel.id), 
            phonenum=restModel.phonenum,
            rating=str(restModel.rating),
            reviewcount=str(restModel.reviewcount))
    writer.commit()

# Location Schema and Index

class LocationSchema(SchemaClass):
    id = ID(stored=True)
    address = KEYWORD(stored=True)
    neighborhood = KEYWORD(stored=True)
    zipcode = KEYWORD(stored=True)
    latitude = ID(stored=True)
    longitude = ID(stored=True)

def get_location_index():
    if(index.exists_in(whoosh_index_path, indexname="location_index")):
        loc_ix = index.open_dir(whoosh_index_path, indexname="location_index")
    else:
        loc_ix = index.create_in(whoosh_index_path, schema=LocationSchema(), 
            indexname="location_index")
        fill_location_index(loc_ix)
    return loc_ix
    
def fill_location_index(ix):
    writer = ix.writer()

    locModelList = Location.query.filter_by().all()
    for locModel in locModelList:
        writer.add_document(address=locModel.address, 
            id=str(locModel.id), 
            neighborhood=locModel.neighborhood,
            zipcode=str(locModel.zipcode),
            latitude=str(locModel.latitude),
            longitude=str(locModel.latitude))
    writer.commit()

# Category Schema and Index

class CategorySchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True)
    resttotal = ID(stored=True)
    reviewtotal = ID(stored=True)
    ratingavg = ID(stored=True)

def get_category_index():
    if(index.exists_in(whoosh_index_path, indexname="category_index")):
        logger.debug("GETTING CATEGORY INDEX")
        cat_ix = index.open_dir(whoosh_index_path, indexname="category_index")
    else:
        logger.debug("CREATING CATEGORY INDEX")
        cat_ix = index.create_in(whoosh_index_path, schema=CategorySchema(), 
            indexname="category_index")
        fill_category_index(cat_ix)
    return cat_ix
    
def fill_category_index(ix):
    logger.debug("FILLING CATEGORY INDEX")
    writer = ix.writer()
    logger.debug("FILLING CATEGORY INDEX2")
    catModelList = Category.query.filter_by().all()
    for catModel in catModelList:
        logger.debug(catModel.id)
        writer.add_document(name=catModel.name, 
            id=str(catModel.id), 
            resttotal=str(catModel.resttotal),
            reviewtotal=str(catModel.reviewtotal),
            ratingavg=str(catModel.ratingavg))
    writer.commit()

def search_results(ix, search_query, fields):
    qp = MultifieldParser(fields, schema=ix.schema, group=qparser.OrGroup)
    q = qp.parse(search_query)
    data = []
    data_index = 0

    with ix.searcher() as s:
        results = s.search(q)
        logger.debug(results)
        for hit in results:
            logger.debug(hit)
            data.append(dict(**hit))
            context = str()
            for field in fields:
                if(len(hit.highlights(field)) > 0):
                    context += hit.highlights(field)
            data[data_index]["context"] = context
            data_index += 1
    return data
