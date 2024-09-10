import requests

API_URL = "https://api.openbrewerydb.org/v1/breweries/random"

def get_brewery_data():
    response = requests.get(API_URL)
    return response.json()[0]

