# cs373-idb

Python Web application based on providing information about Austin restaurants, inspired by IMDB and Yelp.

[![Build Status](https://travis-ci.org/brockuniera/cs373-idb.svg?branch=master)](https://travis-ci.org/brockuniera/cs373-idb)

## Database Model

Restaurant - Information about restaurants such as location, name, category, price and rating.
  * ex. Hula Hut, ...
  
Location - Information about restaurant locations such as address, zip code, latitude, longitude and neighborhood.
  * ex. 6th Street, 78701, ...
  
Category - Information such as name, total number of restaurants in this category and average price for this category of restaurants.
  * ex. Mexican, ... 
    
##How to run locally  

1. Clone the project

2. Open terminal and go into the cloned repository, then cd app.

3. Run "pip install -r requirements.txt" to download dependencies required for the application onto your own machine.

4. To query the Yelp API you will need to acquire a [API key](https://www.yelp.com/developers/manage_api_keys) from them.

5. Then follow [these instructions](https://github.com/Yelp/yelp-python) to create a config_secret.json file that holds your private API key information. 

6. Execute app.py by running "python app.py".

7. In order to view the site, open a browser and go to 127.0.0.1:5000.
