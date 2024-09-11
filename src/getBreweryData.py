import requests

API_URL_BASE = "https://api.openbrewerydb.org/v1/breweries"

def get_random_brewery():
    response = requests.get(API_URL_BASE + "/random")
    return response.json()[0]

