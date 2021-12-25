from app import app
from flask import render_template, redirect, url_for, request
from app.forms import SearchForm
from app.weather import WeatherForecast
import requests, os

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
    return render_template('204.html')

  if len(woeid) > 1:
    data = weather.get_weather(woeid)
    return render_template('select.html', data=data)

  data = weather.get_weather(woeid)
  today_icon = os.path.join(app.config['UPLOAD_FOLDER'], f'{data[0]["consolidated_weather"][0]["weather_state_abbr"]}.png')

  # next 5 days
  next_days_forecast = weather.next_day_forecast(data)

  icon = list()

  for i in next_days_forecast:
    icons = os.path.join(app.config['UPLOAD_FOLDER'], f'{i["weather_state_abbr"]}.png')
    icon.append(icons)

  # convert day to str
  day_str = weather.convert_day_str(data)
  
  return render_template('index.html', data=data, form=form, next_days=next_days_forecast, icons=icon, today_icon=today_icon, day_str=day_str)


# if output woeid > 1
@app.post('/select')
@app.get('/select')
def select():
  form = SearchForm()
  weather = WeatherForecast()

  if request.method == "POST":
    woeid = ["".join(list(request.form.get('city')))]
    data = weather.get_weather(woeid)
    today_icon = os.path.join(app.config['UPLOAD_FOLDER'], f'{data[0]["consolidated_weather"][0]["weather_state_abbr"]}.png')


    next_days_forecast = weather.next_day_forecast(data)
    icon = list()

    for i in next_days_forecast:
      icons = os.path.join(app.config['UPLOAD_FOLDER'], f'{i["weather_state_abbr"]}.png')
      icon.append(icons)

      # convert day to str
    day_str = weather.convert_day_str(data)
  
    return render_template('index.html', form=form, data=data, next_days=next_days_forecast, icons=icon, today_icon=today_icon, day_str=day_str)

  return redirect(url_for('index'))