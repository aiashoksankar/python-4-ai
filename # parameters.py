# parameters 
# pass data into your functions 

# Parameters let you pass data into functions. Instead of hardcoding values, you make functions flexible to work with different inputs. 
# positional parameters 
def greet(name):
 print(f'hello {name}!')
greet('Alice')
greet('sam')
greet('raju')

# keyword parameters 

def intro(name,age):
 print(f"my name is {name}")
 print(f'i m {age} old')

intro(name="alice",age=20)
intro(age=25,name="ariv")

# multiple parametes 
def cal(price,tax,discount):
  tax=price*tax
  final_price=price + tax - discount
  print(f'total:${final_price}')

cal(100,0.99,10) #positional parameters 


# defalt values 
def greet(name,greeting="hello"):
 print(f'{greeting},{name}!')

# use default 
greet("alice")

# override 
greet("bob","hi")
greet("charlie","hey")

# key word arguments 
def profile(name,age,city):
 print(f'{name},{age} from {city}')

#  positional arguments 
profile("alice",25,'nyc')

# keyword arguments 
profile(city="chennai",age=25,name="alice")
profile(city="washington",name="lajja",age=30)






