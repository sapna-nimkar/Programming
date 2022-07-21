'''

'''

class Dog:
    count = 0
    #private class variable
    __instance = None

    def __init__(self, name):
        if Dog.__instance is None:
            self.name = name
            self.__class__.count += 1
            Dog.__instance = self
        else:
            raise Exception("cannot instantate. use get_instance()")

    #static method
    @staticmethod
    def get_instance(name):
        if Dog.__instance is None:
            Dog(name)
        return Dog.__instance


joey = Dog("Joey")
jenny = Dog("Jenny")
daisy = Dog("Daisy")
sheru = Dog.get_instance("Sheru")
print(sheru)

#instance variable  = name -> attached to the self
#class variable = count -> no relation with self

#to prnt joeys name
print(joey.name)
print(joey.__class__.count)

