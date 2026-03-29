# data structures tuple 
# Work with immutable sequences

# ​
# What are tuples?
# Tuples are like lists, but they can’t be changed once created. They’re immutable (unchangeable) sequences.
# Use tuples for data that shouldn’t change:
# Coordinates (x, y)
# RGB colors (255, 0, 0)
# Database records
# Function return values

# creating tuples 
empty=()

point =(3,5)
colors=("red","green","blue")

# single item tuple needs comma 
single=(42,)
not_tuple=(42)

coordinates=10,12 

# accessing items
point=(3,5)
colors=("red","green","blue")

# get items
print(point[0])
print(colors[-1])

# slicing
print(colors[0:3])

# tuple unpacking  -Python’s coolest tuple feature:
point=(3,5)
x,y= point
print(x)
print(y)

# multiple assignment 
a,b,c=1,2,3

# swap variables 
x,y=y,x

# rigt create a new tuple 
point=(4,point[1])
# or convert to list,modify,covert back 
tempp=list(point)
tempp[0]=4
point=tuple[tempp]














