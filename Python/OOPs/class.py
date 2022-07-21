'''
Concepts of Class and how , when its used
refernce: Geek4geek
'''

#class is a BLUEPRINT of object. Class is stateless
class Dog:

    #class attribute/property/variable
    attr1 = "mammal"
    count = 0
    #instance attribute
    def __init__(self, name):
        self.name = name
        self.__class__.count += 1
        # this s equivalent to Dog.count += 1
    
    #instance method
    def speak(self):
        print(f'My name is {self.name} WOOF!')
    
    @staticmethod
    def animal_catgory():
        return "Dog"


#Driver Code , Instantiating the objects of the class

#Object: real entity with some states 



Dog.animal_catgory()

joey = Dog("Joey")

jenny = Dog("Jenny")
print(f"Count: {Dog.count}")
#accessing Class Attribute
Dog.attr1 = "Dog"
print(f'Roger is a {joey.__class__.attr1}')
print(f'Jenny is a {Dog.attr1}')

#accessing Instance attributes
print("My name is {}".format(joey.name))
print("My name is {}".format(jenny.name))

#Accesing Instance Methods
joey.speak()
jenny.speak()







