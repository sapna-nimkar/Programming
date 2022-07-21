

class Dog:
    #define a priovate varable class variable
    __instance = None
# below we are preventing the creation of object more than once
    def __init__(self, name):
        if Dog.__instance is None:
            self.name = name
            Dog.__instance = self
        else:
            raise Exception("use get_instance()")

#static method : if someone want to create/get the reference of Singleton object, either by creating new or referencing to the old, we are creating helper method
    @staticmethod
    def get_instance(name):
        if Dog.__instance is None:
            Dog(name)
        return Dog.__instance

joey = Dog.get_instance("Joey the fluffy")
#sheru = Dog("Sheru the furry")
sheru = Dog.get_instance("Sheru the furry")
print(joey.name)
print(sheru.name)


class DatabaseConn:

    #priivate class variable
    __instance = None

    def __init__(self, host, port, username, password):

        if DatabaseConn.__instance == None:
            self.host = host
            self.port = port
            self.username = port
            self.password = password
            self.conn = connect(host, port, username, password)
            DatabaseConn.__instance = self
        else:
            raise Exception(" use get_instance method")

    @staticmethod
    def get_instance(host, port, username, password):
        if DatabaseConn.__instance == None:
            DatabaseConn(host, port, username, password)
        return DatabaseConn.__instance
    
    def __del__(self):
        DatabaseConn.__instance.conn.close()
        DatabaseConn.__instance = None


conn_three = DatabaseConn(h,p,u,p)
conn_one = DatabaseConn.get_instance(h,p,u,p)
conn_two = DatabaseConn.get_instance(h,p,u,p)

del conn_one





