# methods  and attributes 
""" 
# syntax 
class Apiclient:
    def __init__(self,api_key,base_url):
        self.api_key,base_url
        self.request_count=0
#creating instance with named args
client1=Apiclient(api_key="key1",base_url="https://api1.com")
client2=Apiclient(api_key="key2",base_url="https://api2.com")

# syntax 1 
class Apiclient:
    version="1.0"
    max_retries=3

def __init__(self,apikey):
    self.apikey=apikey """ 

# methods:adding behaviour 
class datavalidator:
    def __init__(self):
        self.errors=[]

def validate_email(self,email):
    if "@" not in email:
      self.errors.append(f'invalid email:{email}')
      return False
    return True

def validate_age(self,age):
    if age>0 or age>150:
        self.errors.append(f'invalid age:{age}')
        return False
    return True

def get_errors(self):
    return self.errors

# use the validator 
validator=datavalidator()

# we dont pass self, just email 
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

print(validator.get_errors())































