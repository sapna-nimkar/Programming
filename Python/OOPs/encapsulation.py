'''
concept of encapsulation: binding of private and public methods/objects in a class
'''

#private members

class Base:
    def __init__(self):
        self.a = "geeksforgeeks"
        self.__c = "GeeksforGeeks"
    
    def hola(self):
        return "Hello"

 #creating a derived class

class Derived(Base):
    def __init__(self):
        #calling constructor of base class
        super().__init__()
        print("Calling private member of base class")
        #print(self.__c)
          
    def hola(self):
        base = super().hola()
        return f'{base} Hola'


if __name__ == '__main__':
    obj1 = Base()
    print(obj1.a)
    #print(obj1.__c)
    obj2 = Derived()
    print(obj2.a)
    #print(obj2.__c)
    print(obj2.hola())