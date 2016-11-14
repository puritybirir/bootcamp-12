#!/usr/bin/env python

import requests
from pprint import pprint
def get_makeup():
	"""Gets a list of makeup products and their various descriptions."""

    #send a get request
	response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?brand=covergirl&product_type=lipstick")

	if response.status_code != 200:
		raise Exception("API error. Response status: {}".format(response.status_code))
	else:
		return response.json