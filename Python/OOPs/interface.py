"""
# Declaration vs Defination
Declaration is writing the signature i.e. name of function, return type, arguments etc
def hello(name: str) -> str:

Defination is the implementation of method
def hello(name: str) -> str:
    message = f"Hello {name}!"
    print(message)
    return message

# Why to use interface?
It sets behavior(methods) of a class (to be implemented)

An interface in Java is a blueprint of a class. 
A Java interface contains static constants(variable) and abstract methods.

interface Calculator{
    int static a = 10;
    int sum();
    float sum();
    
}

public class ClassName extends ParentClass1{

}

public class ClassName implements Interface1, Interface2{
    public int sum(){

    }
}


# Python 

In python interface can be acheived by inheriting Abstract Base Class (ABC)
If child class doesn't immplement parent's abstract method it gets(Exception) TypeError
"""
from abc import ABC, abstractmethod 


class HumanAbstract(ABC):
    @abstractmethod
    def walk():
        pass    
    @abstractmethod
    def talk():
        pass

    def sing(self):
        print(f"{self.name} is singing")


class Human(HumanAbstract):
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(f"My name is {self.name.capitalize()}")
    
    def walk(self):
        print(f"{self.name} is walking")
    
    def talk(self):
        print(f"{self.name} is talking")


if __name__ == '__main__':
    name = 'super'
    supratin  = Human(name)
    supratin.print_name()
    supratin.sing()

    sapna = HumanAbstract()