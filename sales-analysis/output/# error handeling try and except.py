# error handeling try and except 

""" try:
    # Code that might cause an error
    risky_operation()
except:
    # Code that runs if there's an error
    print("Something went wrong")"""


# catching specfic error 
# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here


print("hi there!")

# basic syntax 
try:
    # code that might cause an error 
    risky_operation()
except:
    # code that runs if thers an error 
    print("something went wrong")

    # catching specific error 
try:
        age=int(input("enter your age:"))
        print(f"in 10 years ,you'll be {age+10}")
except ValueError:
     print("please enter a number:")

# multiple error types 
try:
    #  read a number from a title 
 with open ('number.txt',y) as f:
    text=f.read()
    number=int(text)
   result=100/number
 print(f"result:{result}")
except FileNotFoundError:
    print("could not find number.txt")
except ValueError:
    print("file doesnot contain a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")

# the else clause
try:
    with open('data.txt','r') as f:
        data=f.read()
except FileNotFoundError:
    print("file not found ")
else:
    print(f'File has {len(data)} char')

# finally clause

try:
    file=open('data.txt','r')
    data=file.read()
except FileNotFoundError:
    print("file not found")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("cleanup complete")
    





























