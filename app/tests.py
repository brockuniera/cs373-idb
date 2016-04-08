from unittest import main, TestCase

from db import app, db
from models import Restaurant, Location, Category

_TEST_DATABASE_URI = 'sqlite://'
# app.config['SQLALCHEMY_DATABASE_URI'] = _TEST_DATABASE_URI

_RESTDICTS = [
    {
        "imageurl": "imageurl",
        "name": "Test Name",
        "phonenum": 5125551234,
        "url": "aurl",
        "rating": 2.0,
        "reviewcount": 100,
    },
    {
        "imageurl": "imageurl2",
        "name": "Olive Garden",
        "phonenum": 1233457899,
        "url": "aurl2",
        "rating": 3.0,
        "reviewcount": 1000,
    },
    {
        "imageurl": "imageurl3",
        "name": "Hula Hut",
        "phonenum": 5125557893,
        "url": "aurl3",
        "rating": 1.0,
        "reviewcount": 1,
    },
]

_LOCDICTS = [
    {
        "address": "north pole",
        "neighborhood": "arctic",
        "zipcode": 78727,
        "latitude": 0.12345,
        "longitude": -1.12345,
    },
    {
        "address": "1111 nowhere lane",
        "neighborhood": "Downtown",
        "zipcode": 78701,
        "latitude": 12.12345,
        "longitude": -97.12345,
    },
    {
        "address": "9999 somewhere st",
        "neighborhood": "dirty 6th",
        "zipcode": 78791,
        "latitude": 2.13459,
        "longitude": -9.12385,
    },
]

_CATDICTS = [
    {
        "name": "Mexican",
        "resttotal": 110,
        "reviewtotal": 990,
        "ratingavg": 4.1,
    },
    {
        "name": "Italian",
        "resttotal": 999,
        "reviewtotal": 1,
        "ratingavg": 5.0,
    },
    {
        "name": "Japanese",
        "resttotal": 1,
        "reviewtotal": 500,
        "ratingavg": 1.0,
    },
]

class TestFood(TestCase):
    def test_create_restaurant_0(self):
        data = _RESTDICTS[0]
        test_restaurant = Restaurant(**data)
        self.assertEqual(data["imageurl"], test_restaurant.imageurl)
        self.assertEqual(data["name"], test_restaurant.name)
        self.assertEqual(data["phonenum"], test_restaurant.phonenum)
        self.assertEqual(data["rating"], test_restaurant.rating)
        self.assertEqual(data["reviewcount"], test_restaurant.reviewcount)
        self.assertEqual(data["url"], test_restaurant.url)

    def test_create_restaurant_1(self):
        data = _RESTDICTS[1]
        test_restaurant = Restaurant(**data)
        self.assertEqual(data["imageurl"], test_restaurant.imageurl)
        self.assertEqual(data["name"], test_restaurant.name)
        self.assertEqual(data["phonenum"], test_restaurant.phonenum)
        self.assertEqual(data["rating"], test_restaurant.rating)
        self.assertEqual(data["reviewcount"], test_restaurant.reviewcount)
        self.assertEqual(data["url"], test_restaurant.url)

    def test_create_restaurant_2(self):
        data = _RESTDICTS[2]
        test_restaurant = Restaurant(**data)
        self.assertEqual(data["imageurl"], test_restaurant.imageurl)
        self.assertEqual(data["name"], test_restaurant.name)
        self.assertEqual(data["phonenum"], test_restaurant.phonenum)
        self.assertEqual(data["rating"], test_restaurant.rating)
        self.assertEqual(data["reviewcount"], test_restaurant.reviewcount)
        self.assertEqual(data["url"], test_restaurant.url)

    def test_create_location_0(self):
        data = _LOCDICTS[0]
        test_location = Location(**data)
        self.assertEqual(data["address"], test_location.address)
        self.assertEqual(data["neighborhood"], test_location.neighborhood)
        self.assertEqual(data["zipcode"], test_location.zipcode)
        self.assertEqual(data["latitude"], test_location.latitude)
        self.assertEqual(data["longitude"], test_location.longitude)

    def test_create_location_1(self):
        data = _LOCDICTS[1]
        test_location = Location(**data)
        self.assertEqual(data["address"], test_location.address)
        self.assertEqual(data["neighborhood"], test_location.neighborhood)
        self.assertEqual(data["zipcode"], test_location.zipcode)
        self.assertEqual(data["latitude"], test_location.latitude)
        self.assertEqual(data["longitude"], test_location.longitude)

    def test_create_location_2(self):
        data = _LOCDICTS[2]
        test_location = Location(**data)
        self.assertEqual(data["address"], test_location.address)
        self.assertEqual(data["neighborhood"], test_location.neighborhood)
        self.assertEqual(data["zipcode"], test_location.zipcode)
        self.assertEqual(data["latitude"], test_location.latitude)
        self.assertEqual(data["longitude"], test_location.longitude)

    def test_create_category_0(self):
        data = _CATDICTS[0]
        test_category = Category(**data)
        self.assertEqual(data["name"], test_category.name)
        self.assertEqual(data["resttotal"], test_category.resttotal)
        self.assertEqual(data["reviewtotal"], test_category.reviewtotal)
        self.assertEqual(data["ratingavg"], test_category.ratingavg)

    def test_create_category_1(self):
        data = _CATDICTS[1]
        test_category = Category(**data)
        self.assertEqual(data["name"], test_category.name)
        self.assertEqual(data["resttotal"], test_category.resttotal)
        self.assertEqual(data["reviewtotal"], test_category.reviewtotal)
        self.assertEqual(data["ratingavg"], test_category.ratingavg)

    def test_create_category_2(self):
        data = _CATDICTS[2]
        test_category = Category(**data)
        self.assertEqual(data["name"], test_category.name)
        self.assertEqual(data["resttotal"], test_category.resttotal)
        self.assertEqual(data["reviewtotal"], test_category.reviewtotal)
        self.assertEqual(data["ratingavg"], test_category.ratingavg)

    def test_relationship_restaurant_category_0(self):
        testrest = Restaurant(**_RESTDICTS[0])
        fatcat = Category(**_CATDICTS[0])

        self.assertEqual(len(testrest.catlist), 0)
        self.assertEqual(len(fatcat.restlist), 0)

        testrest.catlist.append(fatcat)

        self.assertEqual(len(testrest.catlist), 1)
        self.assertEqual(len(fatcat.restlist), 1)

        self.assertEqual(testrest.catlist[0], fatcat)
        self.assertEqual(fatcat.restlist[0], testrest)

    def test_relationship_restaurant_category_1(self):
        testrest = Restaurant(**_RESTDICTS[0])
        fatcat = Category(**_CATDICTS[0])

        self.assertEqual(len(testrest.catlist), 0)
        self.assertEqual(len(fatcat.restlist), 0)

        fatcat.restlist.append(testrest)

        self.assertEqual(len(testrest.catlist), 1)
        self.assertEqual(len(fatcat.restlist), 1)

        self.assertEqual(testrest.catlist[0], fatcat)
        self.assertEqual(fatcat.restlist[0], testrest)

class TestRestaurants(TestCase):

    def setUp(self):
        db.create_all()
        self.rest1 = Restaurant(**_RESTDICTS[0])
        self.rest2 = Restaurant(**_RESTDICTS[1])
        db.session.add(self.rest1)
        db.session.add(self.rest2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_rests(self):
        rests = Restaurant.query.all()
        self.assertEqual(len(rests), 2)

    def test_repr(self):
        rest = Restaurant.query.filter_by(name='Test Name').one()
        correctreprfstring = "<Restaurant(imageurl='{imageurl}', name='{name}', phonenum='{phonenum}', rating='{rating}', reviewcount='{reviewcount}', url='{url}')>"
        self.assertEqual( repr(rest), correctreprfstring.format(**_RESTDICTS[0]))

    def test_filtering_rests_0(self):   
        rest = Restaurant.query.filter_by(name='Test Name').one()
        self.assertEqual(rest, self.rest1)

    def test_filtering_rests_1(self):   
        rest = Restaurant.query.filter(Restaurant.rating < 3.0).first()
        self.assertEqual(rest, self.rest1)

    def test_add_delete_rests(self):
        rest3 = Restaurant(**_RESTDICTS[2])
        db.session.add(rest3)
        db.session.commit()
        self.assertEqual(len(Restaurant.query.all()), 3)
        Restaurant.query.filter_by(name='Test Name').delete()
        db.session.commit()
        self.assertEqual(len(Restaurant.query.all()), 2)

    def test_get_data_names_0(self):
        self.assertEqual(len(Restaurant.getDataNames()), 5)

    def test_get_data_names_1(self):
        self.assertEqual(Restaurant.getDataNames(), ["id", "name", "phonenum", "rating", "reviewcount"])

    def test_get_data_names_2(self):
        self.assertEqual(Restaurant.getDataNames()[0], "id")

class TestLocations(TestCase):

    def setUp(self):
        db.create_all()
        self.loc1 = Location(**_LOCDICTS[0])
        self.loc2 = Location(**_LOCDICTS[1])
        db.session.add(self.loc1)
        db.session.add(self.loc2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_locs(self):
        locs = Location.query.all()
        self.assertEqual(len(locs), 2)

    def test_repr(self):
        loc = Location.query.filter_by(address=_LOCDICTS[0]['address']).one()
        correctreprfstring = "<Location(address='{address}', neighborhood='{neighborhood}', zipcode='{zipcode}', latitude='{latitude}', longitude='{longitude}')>"
        self.assertEqual( repr(loc), correctreprfstring.format(**_LOCDICTS[0]))

    def test_filtering_locs_0(self):   
        loc = Location.query.filter_by(address=_LOCDICTS[0]['address']).one()
        self.assertEqual(loc, self.loc1)

    def test_filtering_locs_1(self):   
        loc = Location.query.filter(Location.zipcode == _LOCDICTS[0]['zipcode']).first()
        self.assertEqual(loc, self.loc1)

    def test_add_delete_locs(self):
        loc3 = Location(**_LOCDICTS[2])
        db.session.add(loc3)
        db.session.commit()
        self.assertEqual(len(Location.query.all()), 3)
        Location.query.filter_by(address=_LOCDICTS[2]['address']).delete()
        db.session.commit()
        self.assertEqual(len(Location.query.all()), 2)

    def test_get_data_names_0(self):
        self.assertEqual(len(Location.getDataNames()), 6)

    def test_get_data_names_1(self):
        self.assertEqual(Location.getDataNames(), ["id", "address", "neighborhood", "zipcode", "latitude", "longitude"])

    def test_get_data_names_2(self):
        self.assertEqual(Location.getDataNames()[0], "id")

class TestCategorys(TestCase):

    def setUp(self):
        db.create_all()
        self.cat1 = Category(**_CATDICTS[0])
        self.cat2 = Category(**_CATDICTS[1])
        db.session.add(self.cat1)
        db.session.add(self.cat2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_cats(self):
        cats = Category.query.all()
        self.assertEqual(len(cats), 2)

    def test_repr(self):
        cat = Category.query.filter_by(name=_CATDICTS[0]['name']).one()
        correctreprfstring = "<Category(name='{name}', resttotal='{resttotal}', reviewtotal='{reviewtotal}', ratingavg='{ratingavg}')>"
        self.assertEqual(repr(cat), correctreprfstring.format(**_CATDICTS[0]))

    def test_filtering_cats_0(self):   
        cat = Category.query.filter_by(name=_CATDICTS[0]['name']).one()
        self.assertEqual(cat, self.cat1)

    def test_filtering_cats_1(self):   
        cat = Category.query.filter(Category.ratingavg > _CATDICTS[0]['ratingavg']).one()
        self.assertEqual(cat, self.cat2)

    def test_add_delete_cats(self):
        cat3 = Category(**_CATDICTS[2])
        db.session.add(cat3)
        db.session.commit()
        self.assertEqual(len(Category.query.all()), 3)
        Category.query.filter_by(reviewtotal=_CATDICTS[2]['reviewtotal']).delete()
        db.session.commit()
        self.assertEqual(len(Category.query.all()), 2)

    def test_get_data_names_0(self):
        self.assertEqual(len(Category.getDataNames()), 5)

    def test_get_data_names_1(self):
        self.assertEqual(Category.getDataNames(), ["id", "name", "resttotal", "reviewtotal", "ratingavg"])

    def test_get_data_names_2(self):
        self.assertEqual(Category.getDataNames()[0], "id")

if __name__ == '__main__':
    main()
