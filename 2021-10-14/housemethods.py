#!/usr/bin/python3
from house import House

house1 = House()
house1.set_address("1 Bassil Street,Kogarah,NSW,Australia")

try:
    house1.set_doors(5)
    house1.set_windows(14)
except ValueError:
    print("Please provide a valid input")

house1.p_out()
house1.set_lock()
house1.enter()
house1.set_unlock()
house1.enter()









