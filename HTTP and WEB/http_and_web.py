#!/usr/bin/env python

import requests
from pprint import pprint
def main():
	'''A weather application that shows the weather of a city and its temparature '''
	city= "Nairobi"
	response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=31cb387d5a46c10fe1e0400a04d0721f&units=metric")
	assert response.status_code == 200

	weather=response.json()
	print("The weather for",weather['name'])
	print(weather['main']['temp'])
	print(weather['weather'][0]['description'])

	if response.status_code != 200:
		raise Exception("API error. Response status: {}".format(response.status_code))
	else:
		return response.json

if __name__ == '__main__':
	main()

	