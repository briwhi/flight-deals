# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta


flight_search = FlightSearch()
data_manager = DataManager()


sheet_data = data_manager.get_sheety_data()
if sheet_data["prices"][0]["iataCode"] == '':
    for city in sheet_data["prices"]:
        iata_code = flight_search.find_iata(city["city"])
        row = city["id"]
        data_manager.update_iata_on_sheet(row, iata_code)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

