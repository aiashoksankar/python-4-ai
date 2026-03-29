import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"

# if you want to access the befor hierrchy folder use ../data 4

if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")


    """
Best practices
Keep data separate - Don’t mix code and data files
Use clear names - data for input files, output for results
Simple structure - Keep your main script at the project level
Test as you go - Use Shift+Enter to run code step by step"""
