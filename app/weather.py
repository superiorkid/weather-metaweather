import requests

BASE_URL = 'https://www.metaweather.com/api/'

class WeatherForecast:

	def get_city_woeid(self, city_name):
		url = BASE_URL + f'location/search/?query={city_name}'
		response = requests.get(url)
		data = response.json()
		woeid = [str(_id['woeid']) for _id in data]
		return woeid # return a list

	def get_weather(self, woeid):
		forecast = list()

		for i in woeid:
			url = BASE_URL + f'location/{i}/'
			response = requests.get(url)
			data = response.json()
			forecast.append(data)
		return forecast

	def get_image(self):
		pass
      