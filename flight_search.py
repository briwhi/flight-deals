import requests
from config import *
from pprint import pprint


class FlightSearch:

    def find_iata(self, city):
        endpoint = "https://www.air-port-codes.com/api/v1/multi"
        params = {
            "term": city,
        }
        headers = {
            "APC-Auth": AIRPORT_CODES_API_KEY,
            "APC-Auth-Secret": AIRPORT_CODES_SECRET_KEY,
        }
        response = requests.get(url=endpoint, params=params, headers=headers)
        data = response.json()
        iata = data["airports"][0]["iata"]
        return iata

