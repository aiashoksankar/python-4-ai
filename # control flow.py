# control flow
# if else  
temperature=300
if temperature>=30:
 print("It is very hot")
if temperature > 25:
 print("Its hot")
else:
 print("its nice weather") # wrong results

# elif 

temperature=300
if temperature>=30:
 print("It is very hot")
elif temperature > 25:
 print("Its hot")
else:
 print("its nice weather")


# if elif else
score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

    # multiple if 

age=25
weekend="saturday"
holida="sunday"
raining=True
haslicense=True

# both must be true 
if age>=18 and haslicense:
  print("you can drive")
# atleast one must be true 
if weekend or holiday:
  print("no work today")
if not raining:
  print("lets go outside")

# nested if 
has_ticket=15
age=15

if has_ticket:
  if age>=18:
    print("enjoy the movie")
  else:
    print("adult supervision needed")
else:
  print("buy a ticket first")

