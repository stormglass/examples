import requests

response = requests.get(
    'https://api.stormglass.io/point?lat=58.5&lng=17.8',
    headers={
        'Authorization': 'YOUR API KEY'  # Get your at https://stormglass.io
    }
)

# Do something with response data.
json_data = response.json()