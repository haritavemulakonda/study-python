#!/usr/bin/python3

# suggested time: 15 mins

# INSTRUCTIONS
#
# Create a class called City.
#
# It has a constructor that takes two arguments: latitude, longitude.
#
# Create a dictionary called "cities" which has a key of the city's
# name.  Instantiate three instances of class City with the supplied
# data, and store these instances in the cities dictionary.
#
# DATA
#
# Brisbane: latitude -27.5 longitude 153.0
# Sydney: latitude -33.9, longitude 151.2
# Melbourne: latitude -37.8, longitude is 144.9


# YOUR WORK GOES HERE.



class City:
    """Creating a Class"""
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

cities = {}

city1 = City("-27.5","153")
city2 = City("-33.9","151.2")
city3 = City("-37.8","144.9")

cities = {"Brisbane" : city1,
           "Sydney" : city2,
           "Melbourne" : city3}


print(cities)
