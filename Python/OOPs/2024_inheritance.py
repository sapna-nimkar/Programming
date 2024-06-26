# INHERITANCE

class Animal:

    # Base class
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am a cute animal")

    def eat(self):
        print("i love eating")


class Dog(Animal):

    # Derived class

    def __init__(self):
        Animal.__init__(self)  # this means we are creating the instance of Animal class
        print("Dog Created")

        # override the base method
    def who_am_i(self):
        # notice the same name of the method
        print("I am a cute DOG")

# POLYMORPHISM
class Panda():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Boo"

class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Mew"

po = Panda("po")
felix = Cat("felix")

print(po.speak())
print(felix.speak())

for pet in [po, felix]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())

pet_speak(po)
pet_speak(felix)


# Abstract method mini example

class Furniture():

    def __init__(self, name):
        self.name = name

    def legs(self):
        raise NotImplementedError("Subclass  must implement this abstract method")

class Table(Furniture):

    def legs(self):
        return self.name + " has 4 legs"

class Stool(Furniture):

    def legs(self):
        return self.name + " has 3 legs"

mytable = Table("table")
mystool = Stool("stool")
print(mytable.legs())
print(mystool.legs())

print("00000000000000000000")
mydog = Dog()
mydog.eat()
mydog.who_am_i()

print("______")
my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()