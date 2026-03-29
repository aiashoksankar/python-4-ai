# functions 
# defining functions 

def greet():
 print("Hello!")
# call the function 
greet() 

# function syntax 
def function_name():
    # Code goes here
    # Must be indented
    pass


# for i in range(0,100):
#    print("i am an ai engineer")

# calling functions 

def say_goodbye():
   print("good boy")
   print("see you later")

   say_goodbye()
   say_goodbye()

# functions with logic 

def check_whether():
   temp=25
   if temp>=30:
    print("Its very hot")
   else:
     print("Its cool")
check_whether()

# variable scope local and global -Variables in Python have a “scope” - where they can be accessed and used.
# local 
def calculated_price():
  price=100
  tax=price * 0.5
  print(f'total:{price+tax}')
calculated_price()

# global 
# global keyword:
counter=0

def increment():
  global counter 
  counter+=1
  increment()
  increment()
print(counter)

# use parameters 
total=0

def addtotal(amount):
  global total
  total+amount

#   good using parameters and return 

def addamounts(current_total,amount):
  return current_total+amount
total=0
total=addamounts(total,10)
total=addamounts(total,20)
print(total)


 






































