from db import db

# This is an association table, needed for the many-to-many
# relationship between Restaurant and Category.
# http://docs.sqlalchemy.org/en/rel_1_0/orm/basic_relationships.html#many-to-many
_assoctable_restcat = db.Table('assoc_restcat',
    db.Column('left_id', db.Integer, db.ForeignKey('restaurants.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('categories.id'))
)

class Restaurant(db.Model):
    """
    Represents a row of a Restaurant table
    """
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    imageurl = db.Column(db.String(256))
    name = db.Column(db.String(256))
    phonenum = db.Column(db.String(20))
    rating = db.Column(db.Float)
    reviewcount = db.Column(db.Integer)
    url = db.Column(db.String(256))

    # Attrs for a one-to-one relationship with Location
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location = db.relationship('Location', back_populates='restaurant')

    # Many-to-many with Category
    catlist = db.relationship('Category', secondary=_assoctable_restcat, back_populates='restlist')

    def __init__(self, imageurl, name, phonenum, rating, reviewcount, url):
        """
        Construct a Restaurant object
        imageurl: a random image uploaded to the restaurant's Yelp page
        name: name of this restaurant, String(256)
        phonenum: phone number of this restaurant, String(20)
        rating: customer rating of this restaurant, a Float between [1, 5]
        reviewcount: number of reviews this restaurant has, Integer
        url: the url of the Yelp page of this restaurant
        """
        self.imageurl = imageurl
        self.name = name
        self.phonenum = phonenum
        self.rating = rating
        self.reviewcount = reviewcount
        self.url = url

    def __repr__(self):
        return "<Restaurant(imageurl='{}', name='{}', phonenum='{}', rating='{}', reviewcount='{}', url='{}')>".format(
                self.imageurl, self.name, self.phonenum, self.rating, self.reviewcount, self.url
                )

    @staticmethod
    def getDataNames():
        return ["id", "name", "phonenum", "rating", "reviewcount"]

class Location(db.Model):
    """
    Represents a row of a Location table
    """
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256))
    neighborhood = db.Column(db.String(40))
    zipcode = db.Column(db.String(10))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Corresponding relation for a one-to-one with Restaurant
    restaurant = db.relationship('Restaurant', back_populates='location', uselist=False)

    def __init__(self, address, neighborhood, zipcode, latitude, longitude):
        """
        Construct a Location object
        address: address of this location, String(256)
        neighborhood: neighborhood of this location, String(40)
        zipcode: zipcode of this location, String(10)
        latitude: Geographical latitude of this location, Float
        logitude: Geographical longitude of this location, Float
        """
        self.address = address 
        self.neighborhood = neighborhood 
        self.zipcode = zipcode 
        self.latitude = latitude 
        self.longitude = longitude 

    def __repr__(self):
        return "<Location(address='{}', neighborhood='{}', zipcode='{}', latitude='{}', longitude='{}')>".format(
                self.address, self.neighborhood, self.zipcode, self.latitude, self.longitude
                )

    @staticmethod
    def getDataNames():
        return ["id", "address", "neighborhood", "zipcode", "latitude", "longitude"]


class Category(db.Model):
    """
    Represents a row of a Category table
    """
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    resttotal = db.Column(db.Integer)
    reviewtotal = db.Column(db.Integer)
    ratingavg = db.Column(db.Float)

    # The many-to-many with Restaurant
    restlist = db.relationship('Restaurant', secondary=_assoctable_restcat, back_populates='catlist')

    def __init__(self, name, resttotal, reviewtotal, ratingavg, restlist=None):
        """
        Construct a Category object
        name: name of this category, such as "Mexican" or "Beer, Wine, and Spirits", String(256)
        resttotal: total number of restaurants in this category
        reviewtotal: total number of reviews of restaurants in this category
        rating: average rating of restaurants in this category
        """
        self.name = name 
        self.resttotal = resttotal 
        self.reviewtotal = reviewtotal  
        self.ratingavg = ratingavg 
        self.restlist = restlist or []

    def __repr__(self):
        return "<Category(name='{}', resttotal='{}', reviewtotal='{}', ratingavg='{}', restlist='{}')>".format(
                self.name, self.resttotal, self.reviewtotal, self.ratingavg, self.restlist
                )

    @staticmethod
    def getDataNames():
        return ["id", "name", "resttotal", "reviewtotal", "ratingavg"]

def getDataDictList(modelList):
    """
    Returns a list of dictionary representations of models
    """
    dataDictList = []
    for model in modelList:
        dataDict = model.__dict__
        dataDict.pop("_sa_instance_state", None) # Weird key added by sqlalchemy
        dataDictList.append(dataDict)
    return dataDictList
