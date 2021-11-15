# Geospatial-Data-Project-

### OBJECTIVE
#### The objective of this project is to indicate the perfect location for a new company in the gaming industry around the world. 
#### The main requirements, among a long list, for the localization of the offices I have considered are:
#### - 30% of the company have at least 1 child --> there should be preschools next to the office
#### - Executives like Starbucks --> there should be a Starbucks nearby
#### - Account managers travel a lot --> there should be a train station nearby
#### - Average age of employees between 25 and 40 --> places to go partying
#### - Maintenance guy likes playing basketball --> a basketball court should be nearby
#
### LOCATION SELECTION
#### Based on the sector of the company, I have selected 3 companies worldwide:
#### 1. Madrid --> as it is my homecity and it has a lot of tech companies already here
#### 2. San Francisco --> the key city for tech companies
#### 3. Tel Aviv --> a city which is gaining a lot of importance for start ups and tech companies
#
### WORKING PROCESS
#### Firstly, I established the coordinates I was going to have as the center of each city to see which one was better for all my requirements. For SF & TA I have taken the main train stations situated at the center of the city, and for Madrid the 'Torre Picasso' building situated next to Nuevos Ministerios train station.
#### I got the above mentioned coordinates with geocode, and then I have made calls to Foursquare API for each requirement. All of this with functions.
#### Secondly, once I had that info, I brought all of it to .json files to import them to Mongo. Once in Mongo, I have calculated the distance using 'Mongo Geoqueries' from each place to my main coordinates established at the start of the project. Once I got the distance I have calculated the mean per category to be able to ponderate later.
#### Finally, after establishing my priorities among my requirements (ie. train stations and bars were the most important requirements to me) I have been able to get a punctuation of each city.
#### The outcome of this exercise has been that Tel Aviv is the best city to locate my office based on my requirements, followed by Madrid and finally San Francisco.
#
### STRUCTURE OF PROJECT FILES
#### This project contains:
#### - One folder of notebooks, with my cleaning functions and my geoqueries.
#### - One SRC folder containing all my functions
# 
### LIBRARIES
#### [sys](https://docs.python.org/3/library/sys.html)
#### [pandas](https://pandas.pydata.org/)
#### [dotenv](https://pypi.org/project/python-dotenv/)
#### [pymongo](https://www.mongodb.com/2)
#### [os](https://docs.python.org/3/library/os.html)
#### [geopandas](https://geopandas.org/)

