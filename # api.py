# api 
""" Working with APIs
Pull data from web services
What is an API?
An API (Application Programming Interface) is like a waiter at a restaurant. You tell it what you want, and it brings you the data.
But APIs do more than just fetch information. They’re the bridges that connect your code to other systems. With APIs, you can:
Pull customer data from your CRM (Salesforce, HubSpot)
Get order information from Shopify or WooCommerce
Send messages through Slack or email services
Use AI models from OpenAI or Anthropic
In the context of AI, APIs are essential. They let you connect AI capabilities to real business data and systems.
Your first API call  """


# Let’s get real weather data using a free weather API: 

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# make requests 

response=requests.get(url)
data=response.json()

print(type(data))
print(data)

temp=data['current']['temperature_2m']

# extract what you need 
import requests
def get_weather(latitude, longitude):
 response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
 data=response.json()
 return data['current']['temperature_2m']

# get temperature from different cities 
paris_temp=get_weather(48.85, 2.35)
london_temp=get_weather(51.50, -0.12)
chennai_temp=get_weather(13.06, 80.23)

print(f'paris temperature{paris_temp}°C')
print(f"London: {london_temp}°C")
print(f"chennai: {chennai_temp}°C")

"""You send a request to the API’s URL with parameters (like coordinates)
The API processes your request and finds the data
You receive JSON data back with the information
You extract the specific parts you need

The pattern is always the same: connect to an API, send requests, get data back, use it in your code. 
APIs are how modern software talks to each other."""
 



















