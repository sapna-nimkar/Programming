'''
*args : arbitrary number of arguments 
**kwargs: arbitrary number of keyword arguments
'''

def myfunc(a: int, b:int, c=0,d=0, e=0):
    #Returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05

print(myfunc(40,60))
print(myfunc(40,60,1022))
#print(myfunc(3,4,5,6,7,2,34)) -> TypeError: myfunc() takes from 2 to 5 positional arguments but 7 were given

def myfunc_arg(*args):

    #args is just a tuple of parameter values
    print(args)

    #you can iiterate through this tuple of values / args
    for item in args:
        print(item)
    return sum(args) * 0.05

print(myfunc_arg(40,60,5,10))

#**kwargs 

def myfunc_kwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('I choose {}'.format(kwargs['fruit']))
    else:
        print('there is no fruit')

myfunc_kwargs(fruit = 'apple', veggie= 'lettuce')


def both_argkwarg(*args, **kwargs):
    print('I would have {} quantity of {}'.format(args[1], kwargs['chips']))
    print(args)
    print(kwargs)
both_argkwarg(10,20,30,44,1,2,food='orange', animal='cat',chips='potato')