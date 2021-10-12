#!/usr/bin/python3





""" Converstion metric to convert miles to kilometers"""
conversion_metric = 0.6213712

""" Function to convert miles to Kilometers """
def miles_to_kms(miles):
	try:
		return float(miles)/conversion_metric
	except ValueError:
		print("Input should be a number")



miles_to_park = input("How many miles to the park? ")
kms_to_park = miles_to_kms(miles_to_park) 
if(kms_to_park != None):
	print("It is", kms_to_park, "km to my park")

miles_to_shop=input("How many miles to the shops? ")
kms_to_shop = miles_to_kms(miles_to_shop)
if (kms_to_shop != None):
	print("It is", kms_to_shop, "km to my shops")

miles_to_work =input("How many miles to work? ")
kms_to_work = miles_to_kms(miles_to_work)
if(kms_to_work != None):
	print("It is", kms_to_work, "km to my work")


