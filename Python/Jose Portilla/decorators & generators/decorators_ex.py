def func():
    return 1

print(func())

def hello():
    return "Hello"

print(hello())

print(hello)
greet = hello
print(greet)
print(greet())
if greet == hello:
    print('greet is same as hello')
if hello == greet:
    print('the other way is also true')

try:
    del hello
    hello()
except NameError as e:
    print(e)
finally:
    print(greet())
    print(greet)

def mellow(name:str):
    print('the mellow() function has been executed')
    print(mellow)

    def kreet():
        print('\t i am kreet()')
        return '\t This is the kreet() function inside mellow()'

    def welcome():
        return '\t this is welcome() inside mellow()'

    print("I will return a function")

    if name == 'Joey':
        return kreet
    else:
        return welcome



my_new_func = mellow('Joey')
print(my_new_func())


def cool():

    def super_cool():
        print('I am very cool')

    return super_cool

some_func = cool()
some_func()

def bello():
    return 'Hi Joey'

def other(some_defined_func):
    print('Other code runs here')
    print(some_defined_func())

other(bello)

def new_decorator(original_function):

    def wrapper_function():

        print('some extra code before the original funct')
        original_function()
        print('some extra code After the original function')

    return wrapper_function()

def func_needs_decorator():
    print('i want to be decorated')

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

@new_decorator
def func_needs_decorated():
    print('i wish to be decorated')

