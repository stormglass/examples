import multiprocessing

#: NOTE: External packages that needs to be installed.
import requests
import tqdm

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()
        session.headers.update({
            'Authorization': '<API KEY>'
        })


def fetch_coordinate(coordinate):
    latitude, longitude = coordinate

    with session.get(
        'https://api.stormglass.io/v1/weather/point',
          params={
            'lat': latitude,
            'lng': longitude,
            'params': 'waveHeight',
            'source': 'icon'
        },
    ) as response:
        # Do something with response data
        data = response.json()


if __name__ == '__main__':
    coordinates = []

    # Create a world wide grid with 1° resolution.
    for latitude in range(-90, 90):
        for longitude in range(-180, 180):
            coordinates.append((latitude, longitude))

    with multiprocessing.Pool(initializer=set_global_session) as pool:

        # Convert iterator to list to trigger fetching all data
        list(
            tqdm.tqdm(

                # Use `imap` to return an iterator to use in `tqdm`
                pool.imap(fetch_coordinate, coordinates),
                total=len(coordinates)
            )
        )