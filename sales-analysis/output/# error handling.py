# error handling 
# types of error 

# syntax error 
if x > 5:
 print("big number")

# runtime error 
# dividion error 
result =10/0

# variable doesnt error 
print(score)

# wrong type 
"hello"+5 #type error

# why handle errors 

# creation pgm  with doesnt exist error
with open('data.txt','r') as f:
  contrnt=f.read()
print("Done!") # Never reaches here if file missing

# hers the program that handles the error 

try:
  with open('data.txt','r') as f:
     content=f.read()
except FileNotFoundError:
  print("could not find data.txt")
  content="default data"
print("done!")








