# string formats

name="ashok"
print(f'my name is {name}')

# string methods
text="python programming"

print(text.upper())
lower=text.lower()
tit=text.title()
print(lower)

# finding and replace


message="I love python programming with python"

# check if something exists
print("python" in message)
print(message.startswith("I"))
print(message.endswith("python"))

# find position
print(message.find("python"))
print(message.count("python"))

# replace
new_message=message.replace("python","sas")
print(new_message)


























