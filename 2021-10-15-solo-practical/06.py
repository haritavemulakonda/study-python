#!/usr/bin/python3

# suggested time: 10 mins

# INSTRUCTIONS:
#
# Give this class a constructor that prints "hi".
#
# Give this class a destructor that prints "bye".

class Spinner:
    """ Defining a constructor"""
    def __init__(self):
        print("Hi")

    def __del__(self):
        print("Bye")

Spinner()
