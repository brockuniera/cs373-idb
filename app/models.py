from db import db

# This is an association table, needed for the many-to-many
# relationship between Restaurant and Category.
# http://docs.sqlalchemy.org/en/rel_1_0/orm/basic_relationships.html#many-to-many
_assoctable_restcat = db.Table('assoc_restcat', Base.metadata,
    db.Column('left_id', db.Integer, ForeignKey('restaurants.id')),
    db.Column('right_id', db.Integer, ForeignKey('categories.id'))
)

class Restaurant(Base):
    """
    Represents a row of a Restaurant table
    """
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    phonenum = db.Column(db.String(20))
    price = db.Column(db.Integer)
    rating = db.Column(db.Float)
    reviewcount = db.Column(db.Integer)

    # Attrs for a one-to-one relationship with Location
    location_id = db.Column(db.Integer, ForeignKey('locations.id'))
    location = db.relationship('Location', back_populates='restaurant')

    # Many-to-many with Category
    catlist = db.relationship('Category', secondary=_assoctable_restcat, back_populates='restlist')

    def __init__(self, name, phonenum, price, rating, reviewcount):
        """
        Construct a Restaurant object
        name: name of this restaurant, String(256)
        phonenum: phone number of this restaurant, String(20)
        price: an Integer within [1, 5], giving this restaurant a price rating
        rating: customer rating of this restaurant, a Float between [1, 5]
        reviewcount: number of reviews this restaurant has, Integer
        """
        self.name = name
        self.phonenum = phonenum
        self.price = price
        self.rating = rating
        self.reviewcount = reviewcount

    def __repr__(self):
        return "<Restaurant(name='{}', phonenum='{}', price='{}', rating='{}', reviewcount='{}')>".format(
                self.name, self.phonenum, self.price, self.rating, self.reviewcount
                )

class Location(Base):
    """
    Represents a row of a Location table
    """
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256))
    streetname = db.Column(db.String(40))
    zipcode = db.Column(db.String(10))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Corresponding relation for a one-to-one with Restaurant
    restaurant = db.relationship('Restaurant', back_populates='location', uselist=False)

    def __init__(self, address, streetname, zipcode, latitude, longitude):
        """
        Construct a Restaurant object
        name: name of this restaurant, String(256)
        phonenum: phone number of this restaurant, String(20)
        price: an Integer within [1, 5], giving this restaurant a price rating
        rating: customer rating of this restaurant, a Float between [1, 5]
        reviewcount: number of reviews this restaurant has, Integer
        """
        self.address = address 
        self.streetname = streetname 
        self.zipcode = zipcode 
        self.latitude = latitude 
        self.longitude = longitude 

    def __repr__(self):
        return "<Location(address='{}', streetname='{}', zipcode='{}', latitude='{}', longitude='{}')>".format(
                self.address, self.streetname, self.zipcode, self.latitude, self.longitude
                )

class Category(Base):
    """
    Represents a row of a Category table
    """
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    resttotal = db.Column(db.Integer)
    reviewtotal = db.Column(db.Integer)
    priceavg = db.Column(db.Float)
    ratingavg = db.Column(db.Float)

    # The many-to-many with Restaurant
    restlist = db.relationship('Restaurant', secondary=_assoctable_restcat, back_populates='catlist')

    def __init__(self, name, resttotal, reviewtotal, priceavg, ratingavg):
        """
        Construct a Category object
        name: name of this category, such as "Mexican" or "Beer, Wine, and Spirits", String(256)
        resttotal: total number of restaurants in this category
        reviewtotal: total number of reviews of restaurants in this category
        priceavg: average price of restaurants in this category
        rating: average rating of restaurants in this category
        """
        self.name = name 
        self.resttotal = resttotal 
        self.reviewtotal = reviewtotal 
        self.priceavg = priceavg 
        self.ratingavg = ratingavg 

    def __repr__(self):
        return "<Category(name='{}', resttotal='{}', reviewtotal='{}', priceavg='{}', ratingavg='{}')>".format(
                self.name, self.resttotal, self.reviewtotal, self.priceavg, self.ratingavg
                )
