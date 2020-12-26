import requests


class DataManager:

    def get_sheety_data(self):
        response = requests.get("https://api.sheety.co/df7c2a686c38e0268088ad29fac4603e/flights/prices")
        print(response.json())
        return response.json()

    def update_iata_on_sheet(self, row, iata):
        endpoint = f"https://api.sheety.co/df7c2a686c38e0268088ad29fac4603e/flights/prices/{row}"
        params = {
            "price": {
                "iataCode": iata,
            }
        }
        response = requests.put(url=endpoint, json=params)
        print(response.text)

