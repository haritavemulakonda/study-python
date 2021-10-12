#!/usr/bin/python3

# 2021-10-12, by Yongli Wang
# newdate, changes by ...

# 1. if __main__, do a simple test
# 2. split functions into one separate file
# 3. have a main program, that prints the three questions

# module: tidy2_module.py
# main:   tidy2_main.py


def validateNumber(n):
    """check if the input is a valid number"""
    try:
        n = float(n)
        if n < 0:
            exit()
        return n
    except:
        print("invalid input")
        exit(1)

def miles_to_kilometers(miles):
    """take miles, return kilometers"""
    return miles / 0.6213712

miles_to_park = input("How many miles to the park? ")
v = validateNumber(miles_to_park)
print("It is", miles_to_kilometers(v), "km to my park")

miles_to_shops = input("How many miles to the shops? ")
v = validateNumber(miles_to_shops)
print("It is", miles_to_kilometers(v), "km to my shops")

miles_to_work = input("How many miles to work? ")
v = validateNumber(miles_to_work)
print("It is", miles_to_kilometers(v), "km to my work")




# MY_MODULE
# def add(a,b):
#     """adds to numbers, returns the sum"""
#     return a + b
#
# if __name__ == "__main__":
#     print(add(2,3))

# MAIN PROGRAM
# import my_module
#
# print(my_module.add(4,5))
