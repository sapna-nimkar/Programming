'''
concepts of polymorphism: when a method behaves differently for different objects
'''

class Bird:

    def intro(self):
        print("there are many types of birds")

    def flight(self):
        print("most birds can fly but some cannot")

class Sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly")

class Ostrich(Bird):

    def flight(self):
        print("Osrich cannot fly")



obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.intro()
obj_bird.flight()
obj_sparrow.intro()
obj_sparrow.flight()
obj_ostrich.intro()
obj_ostrich.flight()


class Dog:
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f"My name is {self.name}"

class Dog:
    def set_name(self, name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f"My name is {self.name}"



joey = Dog()
joey.set_name("Joey")
print(joey)

