# inheritance 

class animal:
  def __init__(self,name):
    self.name=name
  
  def eat(self):
    return f'{self.name} is eating'
  
  def sleep(self):
    return f'(self.name) is sleeping'
  
#   child class 
class goat(animal):
  def mehha(self):
    return f'{self.name} says woof'
#   goat positional parmeters
my_goat=goat("buddy")
# or with named args
my_goat1=goat(name="max")

print(my_goat.eat())
print(my_goat.sleep())


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Pass name to parent's __init__
        self.breed = breed      # Dog-specific attribute
    
    def describe(self):
        return f"{self.name} is a {self.breed}"

# Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

# Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())  # Buddy is a Golden Retriever
print(golden.is_pet)      # True (inherited from Animal)

  




