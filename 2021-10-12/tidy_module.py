#!/usr/bin/python3




""" Converstion metric to convert miles to kilometers"""
conversion_metric = 0.6213712

""" Function to convert miles to Kilometers """
def miles_to_kms(miles):
	try:
		return float(miles)/conversion_metric
	except ValueError:
		print("Input should be a number")


if __name__ == "__main__" :
	print(miles_to_kms(50))
	

	



