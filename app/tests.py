from unittest import main, TestCase

from db import app, db
from models import Restaurant, Location, Category


TEST_DATABSE_URI = "sqlite://"

_RESTDICTS = [
    {
        "imageurl": "imageurl",
        "name": "Test Name",
        "phonenum": 5125551234,
        "url": "aurl",
        "rating": 2,
        "reviewcount": 100,
    },
    {
        "imageurl": "imageurl2",
        "name": "Olive Garden",
        "phonenum": 1233457899,
        "url": "aurl2",
        "rating": 3,
        "reviewcount": 1000,
    },
    {
        "imageurl": "imageurl3",
        "name": "Hula Hut",
        "phonenum": 5125557893,
        "url": "aurl3",
        "rating": 1,
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


if __name__ == '__main__':
    main()
