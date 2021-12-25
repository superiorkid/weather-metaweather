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

	def next_day_forecast(self, data):
		new_list = list()

		for next_day in data:
			for i in range(1, len(next_day['consolidated_weather'])):
				new_list.append(next_day['consolidated_weather'][i])

		return new_list