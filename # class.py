# class  

import requests
from datetime import datetime,timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


today=datetime.now()
weekago=today-timedelta(days=7)
monthago=today-timedelta(month=1)
yearago=today-timedelta(year=1)

start_date=weekago.strftime("%y-%m-%d")
end_date=today.strftime("%y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response=requests.get(url)

data=response.json()
print(data)




























