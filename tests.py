from unittest import main, TestCase
from models import Restaurant, Location, Category

class tests(TestCase):

	def test_create_restaurant_0(self):
		data = {"name": "Test Name", "phonenum": 5125551234,
			"price": 5, "rating": 2, "reviewcount": 100}
		test_restaurant = Restaurant(**data)
		self.assertEqual(data["name"], test_restaurant.name)
		self.assertEqual(data["phonenum"], test_restaurant.phonenum)
		self.assertEqual(data["price"], test_restaurant.price)
		self.assertEqual(data["rating"], test_restaurant.rating)
		self.assertEqual(data["reviewcount"], test_restaurant.reviewcount)
		
	def test_create_restaurant_1(self):
		data = {"name": "Olive Garden", "phonenum": 1233457899,
			"price": 1, "rating": 3, "reviewcount": 1000}
		test_restaurant = Restaurant(**data)
		self.assertEqual(data["name"], test_restaurant.name)
		self.assertEqual(data["phonenum"], test_restaurant.phonenum)
		self.assertEqual(data["price"], test_restaurant.price)
		self.assertEqual(data["rating"], test_restaurant.rating)
		self.assertEqual(data["reviewcount"], test_restaurant.reviewcount)
		
	def test_create_restaurant_2(self):
		data = {"name": "Hula Hut", "phonenum": 5125557893,
			"price": 0, "rating": 1, "reviewcount": 1}
		test_restaurant = Restaurant(**data)
		self.assertEqual(data["name"], test_restaurant.name)
		self.assertEqual(data["phonenum"], test_restaurant.phonenum)
		self.assertEqual(data["price"], test_restaurant.price)
		self.assertEqual(data["rating"], test_restaurant.rating)
		self.assertEqual(data["reviewcount"], test_restaurant.reviewcount)
		
	def test_create_location_0(self):
		data = {"address": "1111 nowhere lane", "neighborhood": "Downtown",
			"zipcode": 78701, "latitude": 12.12345, "longitude": -97.12345}
		test_location = Location(**data)
		self.assertEqual(data["address"], test_location.address)
		self.assertEqual(data["neighborhood"], test_location.neighborhood)
		self.assertEqual(data["zipcode"], test_location.zipcode)
		self.assertEqual(data["latitude"], test_location.latitude)
		self.assertEqual(data["longitude"], test_location.longitude)
		
	def test_create_location_1(self):
		data = {"address": "north pole", "neighborhood": "arctic",
			"zipcode": 78727, "latitude": 0.12345, "longitude": -1.12345}
		test_location = Location(**data)
		self.assertEqual(data["address"], test_location.address)
		self.assertEqual(data["neighborhood"], test_location.neighborhood)
		self.assertEqual(data["zipcode"], test_location.zipcode)
		self.assertEqual(data["latitude"], test_location.latitude)
		self.assertEqual(data["longitude"], test_location.longitude)
		
	def test_create_location_2(self):
		data = {"address": "9999 somewhere st", "neighborhood": "dirty 6th",
			"zipcode": 78791, "latitude": 2.13459, "longitude": -9.12385}
		test_location = Location(**data)
		self.assertEqual(data["address"], test_location.address)
		self.assertEqual(data["neighborhood"], test_location.neighborhood)
		self.assertEqual(data["zipcode"], test_location.zipcode)
		self.assertEqual(data["latitude"], test_location.latitude)
		self.assertEqual(data["longitude"], test_location.longitude)
		
	def test_create_category_0(self):
		data = {"name": "Mexican", "resttotal": 110,
			"reviewtotal": 990, "priceavg": 2.1, "ratingavg": 4.1}
		test_category = Category(**data)
		self.assertEqual(data["name"], test_category.name)
		self.assertEqual(data["resttotal"], test_category.resttotal)
		self.assertEqual(data["reviewtotal"], test_category.reviewtotal)
		self.assertEqual(data["priceavg"], test_category.priceavg)
		self.assertEqual(data["ratingavg"], test_category.ratingavg)
		
	def test_create_category_1(self):
		data = {"name": "Italian", "resttotal": 999,
			"reviewtotal": 1, "priceavg": 1.0, "ratingavg": 5.0}
		test_category = Category(**data)
		self.assertEqual(data["name"], test_category.name)
		self.assertEqual(data["resttotal"], test_category.resttotal)
		self.assertEqual(data["reviewtotal"], test_category.reviewtotal)
		self.assertEqual(data["priceavg"], test_category.priceavg)
		self.assertEqual(data["ratingavg"], test_category.ratingavg)
		
	def test_create_category_2(self):
		data = {"name": "Japanese", "resttotal": 1,
			"reviewtotal": 500, "priceavg": 5.0, "ratingavg": 1.0}
		test_category = Category(**data)
		self.assertEqual(data["name"], test_category.name)
		self.assertEqual(data["resttotal"], test_category.resttotal)
		self.assertEqual(data["reviewtotal"], test_category.reviewtotal)
		self.assertEqual(data["priceavg"], test_category.priceavg)
		self.assertEqual(data["ratingavg"], test_category.ratingavg)


if __name__ == '__main__':
    main()
