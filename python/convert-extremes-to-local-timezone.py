#: NOTE: External packages that needs to be installed.
import arrow
import requests
from timezonefinder import TimezoneFinder

longitude = -35.201
latitude = -5.766

tf = TimezoneFinder(in_memory=True)
timezone = tf.closest_timezone_at(lng=longitude, lat=latitude)

response = requests.get(
  'https://api.stormglass.io/v1/tide/extremes/point',
  params={
    'lat': latitude,
    'lng': longitude
  },
  headers={
    'Authorization': '<ENTER API KEY>'
  }
)

json_data = response.json()

print(f'Distance to station: {json_data["meta"]["station"]["distance"]}')

for extrema in json_data['extremes']:
    print(f'{arrow.get(extrema["timestamp"]).to(timezone).format("dddd HH:mm")}: {extrema["height"]}')