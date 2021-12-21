from app import app
from flask import render_template, redirect, url_for, request
from app.forms import SearchForm
from app.weather import WeatherForecast
import requests

@app.post('/')
@app.get('/')
def index():
  city = 'denpasar' # default value
  form = SearchForm()
  weather = WeatherForecast()
  
  if form.validate_on_submit():
    city = form.cities.data
    form.cities.data  = ''

  # get where on earth ID
  woeid = weather.get_city_woeid(city)

  if not woeid:
    return 'no result found'

  if len(woeid) > 1:
    data = weather.get_weather(woeid)
    return render_template('select.html', data=data)

  data = weather.get_weather(woeid)
  
  return render_template('index.html', data=data, form=form)


# if output woeid > 1
@app.post('/select')
@app.get('/select')
def select():
  form = SearchForm()
  weather = WeatherForecast()

  if request.method == "POST":
    woeid = ["".join(list(request.form.get('city')))]
    data = weather.get_weather(woeid)

    return render_template('index.html', form=form, data=data)

  return redirect(url_for('index'))