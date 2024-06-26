# Objects
# What is Self in method?

# self in Instace Methods of a class is used to refer/access the values related to the Object
"""
class Account:
def __init__(self, n, b) -> None:
self.name = n
self.balance = b

def loan_allowed(self):
Instance(Object) Method
if self.balance > 0:
return self.balance * 10
return 0

def withdraw(self, amount):
if self.balance - amount < 0:
raise ValueError
self.balance -= amount

sapna = Account("Sapna", 10000)
supratim = Account("Supratim", 0)
sapna.loan_allowed()
supratim.loan_allowed()
"""

class Dog():

    # CLASS OBJECT ATTRIBUTES
    # THESE ARE SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        #expect the boolean
        self.spots = spots

    # OPERATIONS / ACTIONS ----> methods
    def bark(self, number):
        print("WOOF! My name is {}. And my number is {}".format(self.name, number))

my_dog = Dog(breed='lab', name= 'Joey', spots= False )
print(type(my_dog))
print(my_dog.breed, my_dog.name, my_dog.spots)
print(my_dog.species)
my_dog.bark(10)

class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        # self.area = radius*radius*self.pi
        self.area = radius*radius*Circle.pi

    #METHOD
    def get_circumference(self):
        circumference = 2 * self.pi * self.radius
        return circumference


my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)


class Animal():
    def __init__(self):
        print('animal created')
        print('ran animal init')
    def who_am_i(self):
        print("I am a cute animal")
    def eat(self):
        print("I love eating")


my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

class Cat(Animal, Dog):

    #Inheriting from bas class Animal

    def __init__(self):
        Dog.__init__(self, 'Lab', 'Joey', 'No')
        print("Cat Created")



my_cat = Cat()
my_cat.who_am_i()
my_cat.eat()
print(my_cat.name)
print(my_cat.breed)
print(my_cat.spots)
my_cat.bark(30)
