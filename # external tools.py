# external tools 
""" External tools
Extend Python with packages

​
Beyond built-in Python
Python comes with many built-in functions, but its real power comes from external packages. These are pre-written code libraries that add new capabilities.
​
What are packages really?
Packages are just Python files containing code - typically combinations of functions (which you’ve learned) and classes (coming later). When you import a package, you’re bringing that functionality into your project.
Two types of packages:
Built-in: Come with Python installation (already in your environment)
External: Downloaded from the internet into your virtual environment folder
Python’s ecosystem
Python has packages for everything:
Web scraping: Extract data from websites
Data analysis: Process spreadsheets and databases
AI/ML: Build intelligent applications
APIs: Connect to online services
Automation: Control your computer

requests - Make web requests
pandas - Work with data tables
beautifulsoup4 - Parse HTML
openai - Use AI models
python-dotenv - Manage secrets
"""

# pattern1
import math
math.sqrt(16)


# pattern 2
from math import sqrt,pi
sqrt(16)


import random

number=random.randint(1,1000)
choice=random.choice(["apple","banana","guva"])

# date time 
import datetime
today=datetime.date.today()
print(today)
import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Extract components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Creating specific date/time
custom_date = datetime.datetime(2026, 3, 22, 19, 55)
print("Custom:", custom_date)

# Date arithmetic
tomorrow = now + datetime.timedelta(days=1)
print("Tomorrow:", tomorrow)

# operating system 
import os
cur_dir=os.getcwd()
print(cur_dir)
import os

# Current working directory
print("CWD:", os.getcwd())

# List files in directory
print("Files:", os.listdir("."))

# Create and remove a directory
os.mkdir("test_dir")
print("After mkdir:", os.listdir("."))
os.rmdir("test_dir")
print("After rmdir:", os.listdir("."))

# Environment variable
home = os.getenv("HOME")
print("Home directory:", home)

# Run a shell command
os.system("echo Hello from OS module")

# json data 
import json
data={'name':'Alice',"age":20}
json_str=json.dumps(data)


# from math import sqrt,pi
# result=sqrt(16)
# cirarea=pi * radius **2

# import with alias 
import pandas as pd
df=pd.DataFrame(data)

""" import everything avoid this 
from math import *
"""

import requests

response=requests.get("https://api.example.com/data")
data=response.json()

# data analysis 
import pandas as pd

data={'name':['alice','bob','charlie'],
      'age':[25,30,35],
      'city':['nyc','la','chicago']}

df=pd.DataFrame(data)
print(df)











                      











