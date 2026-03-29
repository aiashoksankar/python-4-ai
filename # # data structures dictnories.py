# # data structures dictionaries 
# Dictionaries
# Store data with key-value pairs

# ​
# What are dictionaries?
# Dictionaries store data in key-value pairs. Think of them like a real dictionary where you look up a word (key) to find its definition (value).
# Real-world examples:
# Phone book: name > phone number
# Menu: dish > price
# User profile: username > user info

my_dict={}

# dictionary with data 
person={ "name":"alice", "age":30,"city":"new york"}


# differtent ways to create
scores=dict(math=95,english=87,science=92)

# accessing values

person={"name":"alice","age":30,"city":"newyork"}

print(person["name"])
print(person["age"])

# safer with get 
print(person.get("job")) # None (no error)
print(person.get("job","unknown")) # "Unknown" (default)

# changing dictionaries 
person={"name":"alice","age":30}
# add or update 
person["email"]="alice@email.com" # Add new
person["age"]=31  # Update existing

# remove existing
del person["email"]  # Remove by key
age=person.pop("age")  # Remove and return
person.clear() # Remove all items

# dictionary methods 

person={"name":"alice","age":30,"city":"newyork"}

# getall keys, values or items 
print(person.keys())   # dict_keys(['name', 'age', 'city'])
print(person.values()) # dict_values(['Alice', 30, 'New York'])
print(person.items())  # dict_items([('name', 'Alice'), ...])

if "name" in person:
    print("Name found")
else:
    print("name not found")

# update multiple values 
person.update({"age":31,"job":"Engineer"})

# nested dictionaries 
students={"alice":{"age":20,"grade":"a"},
          "bob":{"age":21,"grade":"b"},
          "charlie":{"age":19,"grade":'a'}}

# accessing nested data 
print(students["alice"]["grade"]) #A


















































































