import requests

API_URL_BASE = "https://api.openbrewerydb.org/v1/breweries"

DUMMY_DATA = {
    "name": "TestBrewery",
    "street": "Test St",
    "city": "Testville",
    "state_province": "Testachusetts",
    "postal_code": "01234",
    "country": "USA",
    "phone": "123-456-7890",
    "website_url": "www.testbrewery.com",
    "latitude": "42.13960",
    "longitude": "-72.01664"
}

def get_random_brewery(TEST=False):
    if TEST:
        return DUMMY_DATA

    try :
        response = requests.get(API_URL_BASE + "/random")
        return response.json()[0]
    
    except Exception:
        return DUMMY_DATA

