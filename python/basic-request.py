import requests  #: NOTE: External package that needs to be installed.

response = requests.get(
    'https://api.stormglass.io/v1/weather/point',
    params={
        'lat': 58.5,
        'lng': 17.8
    },
    headers={
        'Authorization': 'YOUR API KEY'  # Get your at https://stormglass.io
    }
)

# Do something with response data.
json_data = response.json()