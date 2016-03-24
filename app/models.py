from db import db

_assoctable_restcat = db.Table('assoc_restcat', Base.metadata,
    db.Column('left_id', db.Integer, ForeignKey('restaurants.id')),
    db.Column('right_id', db.Integer, ForeignKey('categories.id'))
)

class Restaurant(Base):
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
        self.name = name 
        self.resttotal = resttotal 
        self.reviewtotal = reviewtotal 
        self.priceavg = priceavg 
        self.ratingavg = ratingavg 

    def __repr__(self):
        return "<Category(name='{}', resttotal='{}', reviewtotal='{}', priceavg='{}', ratingavg='{}')>".format(
                self.name, self.resttotal, self.reviewtotal, self.priceavg, self.ratingavg
                )
