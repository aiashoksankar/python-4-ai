# data structures sets 
"""Sets
Work with unique collections

What are sets?
 Sets are collections that only store unique values. They automatically remove duplicates.
Think of sets like:
A bag of unique marbles
Guest list (each person once)
Unique tags or categories
Creating sets """

emptyset=set() # NOT {} - that's a dict!


# Set with values - both ways work
numbers={1,2,3,4,5}
fruits=set(["apple","banana","orange"])

# from a list(remove duplicates) 
scores=[85,90,92,90]
unique_scores=set(scores)  # {85, 90, 92}

""""Use set() for empty sets,
 not {}. Empty curly braces create a dictionary!"""


colors={"red","blue"}

# add items 
colors.add("green")
print(colors)

# remove items 
colors.remove("blue")
print(colors)

# discard no error if not found 
colors.discard("yellow")

# check in memebership
if "red" in colors:
 print("red is available")

#  commom uses 

# remove duplicates
names=["alice", "bob","alice","bob","charlie"]
unique_names=list(set(names))
print(unique_names)

# fast membership testing
allowes_user={"alice","bob","charlie"}

if "alice" in allowes_user:
 print("access granted")
 






