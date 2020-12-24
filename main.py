#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint

response = requests.get("https://api.sheety.co/df7c2a686c38e0268088ad29fac4603e/flights/prices")
sheet_data = response.json()
pprint(sheet_data)
if sheet_data["prices"][0]["iataCode"] == '':
    for city in sheet_data["prices"]:
        print(city["city"])