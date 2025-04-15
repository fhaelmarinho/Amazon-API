import requests
import json
from headers import *

url = "https://real-time-amazon-data.p.rapidapi.com/deals-v2"

querystring = {"country":"US","categories":"eletronics","min_product_star_rating":"ALL","price_range":"ALL","discount_range":"ALL"}

headers = {
	"x-rapidapi-key": key,
	"x-rapidapi-host": host
}

response = requests.get(url, headers=headers, params=querystring)
response_json = response.json()

try:
    # Check if the response contains the expected data
    if 'data' in response_json:
        print("Data retrieved successfully.")
        # Save the response to a file only if it contains the expected data
        with open("amazon_data.json", "w") as f:
            json.dump(response_json, f, indent=4)
    else:
        print("No data found in the response.")
except json.JSONDecodeError:
    print("Error decoding JSON response.")

