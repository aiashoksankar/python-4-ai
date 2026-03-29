# api-working with data 
""" Working with data
Analyze and visualize data from APIs

​
Building on APIs
Let’s take the weather API from the previous page and create something useful. We’ll get weather data for the past 7 days, 
analyze it, visualize it, and save it.
This brings together everything you’ve learned: 
APIs, data processing, file handling, and visualization.

pip install requests pandas matplotlib
"""

# Get 7 days of weather
# The Open-Meteo API can give us historical data:
import requests
from datetime import datetime,timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os 
# calculate dates 
today=datetime.now()
two_week_ago=today-timedelta(days=14)

# format dates for API(yyyy-mm-dd) 
start_date=two_week_ago.strftime("%Y-%m-%d")
end_date=today.strftime("%Y-%m-%d")

# get paris weather last week 
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response=requests.get(url)
data=response.json()

print(data)
print(type(data))


# using pandas -using manipulate data


# extract the daily data 
daily_data=data['daily']

# create a dataframe 

df=pd.DataFrame({'date':daily_data['time'],
                 'max_temp':daily_data['temperature_2m_max'],
                 'min_temp': daily_data['temperature_2m_min']})

# convert data strings to datetime 

df['date']=pd.to_datetime(df['date'])

print(df)
# ---------------------------------------------------
"""Visualize the data
Create a simple line chart:"""

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")


























