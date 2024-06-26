# *args = arguments --> passed in as a tuple

# **kwargs = keyword arguments

def my_func(a,b, c=0, d=0, e=0):
    # returns 5% of the sum of a and b

    return sum((a,b,c,d, e)) * 0.05

print(my_func(40,60))

print(my_func(40,60,70))

print(my_func(40,60,70, 100))

def your_func(*args):
    print(args)
    return sum(args) * 0.05

print(your_func(80,70,100,90,40,1,23,87))

# ** kwargs

def joey_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my favourite fruit is {}'.format(kwargs['fruit']))
    elif 'veggie' in kwargs:
        print('my favourite veggie is {}'.format(kwargs['veggie']))
    else:
        print(kwargs)

joey_func(fruit='banana', veggie='capsicum', nonveg='chimkins')
joey_func(veggie='capsicum', nonveg='chimkins')
joey_func(nonveg='chimkins')

def this_func(*args, **kwargs):
    print(args)
    print(kwargs)

    print("i would like to have {} {} please".format(args[2], kwargs['food']))

this_func(10, 20, 30, food='apples', furniture='table', drinks='LIIT')


