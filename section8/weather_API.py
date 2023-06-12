import requests
from dotenv import load_dotenv
import pandas as pd
import json
import os

# create .env with API Key
load_dotenv()
api_key = os.getenv('API_KEY')
print(api_key)
city = input("Enter a city name: ")
response = []

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

# exception handling section--
try:
    # Send a GET request to the API
    response = requests.get(url)
    print(response.text)

    # Status Code check
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        # fail error
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    # connection errors
    print("Connection error occurred:", e)


