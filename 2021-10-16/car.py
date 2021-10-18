#!/usr/bin/python3


class Car:
    """ Creating a class for Car!"""
    def __init__(self,c_name,c_make,c_model):
        self.c_name = c_name
        self.c_make = c_make
        self.c_model = c_model


    def owner_details(self,owner_name,insurance_no):
        self.owner_name = owner_name
        self.insurance_no = insurance_no



    def print_out(self):
        print(f"Car name: {self.c_name}\nCar make: {self.c_make}\nCar model: {self.c_model}")
        print(f"Owner's name is {self.owner_name}")
 



