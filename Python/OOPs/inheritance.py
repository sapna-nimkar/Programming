'''
Concepts of Inheritance in python
'''
#parent class
class Person(object):

    #__init__ is constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
    
    def details(self):
        print('My name is {}'.format(self.name))
        print("ID number: {}".format(self.idnumber))
    #child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        #invoking the __init__ of parent class
        Person.__init__(self, name, idnumber)
        # super().__init__(name, idnumber)

    def details(self):
        # print("my name is {}".format(self.name))
        # print("ID Number: {}".format(self.idnumber))
        super().details()
        print("Post {}".format(self.post))

if __name__ == '__main__':        
#creating an object or an instance
    a = Employee('Sapna', 897365, 2000, "Freelance")
        
    #calling function of class Person using this instance
    a.display()
    a.details()



