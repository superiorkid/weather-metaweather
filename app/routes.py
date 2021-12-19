from app import app
from flask import render_template
from app.forms import SearchForm
from app.weather import WeatherForecast
import requests

@app.post('/')
@app.get('/')
def weather():
  city = 'manchester' # default value
  form = SearchForm()
  weather = WeatherForecast()
  
  if form.validate_on_submit():
    city = form.cities.data
    form.cities.data  = ''

  # get where on earth ID
  woeid = weather.get_city_woeid(city) # output example: ['44123', '17364]
  data = weather.get_weather(woeid)

  return render_template('index.html', cities=len, form=form)
