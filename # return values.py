# return values 
"""Get results back from your functions
Getting results from functions
So far, our functions have printed output
 But often you want functions 
to calculate something and 
give you the result to use elsewhere. """

# this function only prints 
# def add_print(a,b):
#     print(a+b)
# add_print(a=5,b=10)


# # this func returns a value 
def add_return(a,b):
    return a+b

result=add_return(a=5,b=3)
print(f'the result is {result}')



# calculate area \

def cal_area(width,height):
 area=width * height
 area=area * 1.05
#  store areturned value 
room_area=cal_area(10,12)
print(f'room size:{room_area} sq ft')


def double(number):
   return number *2
result=double(5)

total=double(5) + double(3)

print(double(10)) 

if double(7) > 10:
   print("Big number")

#    simple function 
def simfun():
   numbers=[1,2,3,4,5]
   first_number=numbers[0]
   last_number=numbers[-1]
   return first_number,last_number

first_number,last_number=simfun()

# return vs print 

# print 
def get_print(name):
   print(f'hello,{name}!')

# returns value 
def get_return(name):
 return("hello,{name}")

# cant use print versions output 
message=get_print("alice")
print(message)

# can use return versions output

message=get_return('alice') #returns the string
print(message.upper()) #hello Alice 
print(message.lower())








 




