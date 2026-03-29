# Data structures

# lists: like a shopping list
# dictionaries:Like a phone book(name:number)
# tuples:Like coordinates(fixed values)
# sets:like a bag unique item


# # list 
# A shopping list (milk, eggs, bread)
# A to-do list (tasks in order)
# A playlist (songs in sequence) 
# Lists use square brackets [] and items are separated by commas. You can mix different data types in the same list!

my_list=[]
fruits=['apple','banana','orange']
numbers=[1,2,3,4,5]
mixed=['hello',42,True,3.14]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

# slicing
print(fruits[0:2])
print(fruits[1:])
# Lists are mutable - you can change them:

fruits[0]="mango"
print(fruits)

# add items

fruits.append("grape")
fruits.insert(1,"kiwi")

# remove items

fruits.remove("banana")
last=fruits.pop()
del fruits[0]

# list methods

print(len(numbers))
print(numbers.count(1))
print(numbers.index(4))

# sorting
numbers.sort()
print(numbers)

# copy 
new_list=numbers.copy()
print(new_list)

# checking lists 
if "apple" in fruits:
    print("found apple")
    # Check if list is empty
if fruits:
  print("list has items")
else :
   print("list is empty")
   

