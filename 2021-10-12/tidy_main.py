#!/usr/bin/python3
import tidy_module


#This is the main program
miles_to_park = input("How many miles to the park? ")
kms_to_park = tidy_module.miles_to_kms(miles_to_park) 
if(kms_to_park != None):
	print("It is",kms_to_park, "km to my park")

miles_to_shop=input("How many miles to the shops? ")
kms_to_shop = tidy_module.miles_to_kms(miles_to_shop)
if (kms_to_shop != None):
	print("It is",kms_to_shop, "km to my shops")

miles_to_work =input("How many miles to work? ")
kms_to_work = tidy_module.miles_to_kms(miles_to_work)
if(kms_to_work != None):
	print("It is",kms_to_work, "km to my work")


