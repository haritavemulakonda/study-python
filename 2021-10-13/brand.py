#!/usr/bin/python3

class Brand:
    """ Discribes the brands of  aeroplanes"""
    def __init__(self,name_aero_type,aero_brand):
        self.name_aero_type = name_aero_type
        self.aero_brand = aero_brand

    def aero(self):
        print("The name of the aeroplane is {} and is of a {} brand".format(self.name_aero_type,self.aero_brand))

a1 = Brand("Jetway","TATA")
a1.aero()

