'''
Decorators are the wrapper functon which is used to execute some code before
and after the function
Manipulating or adding extra functiionality to existing function
'''


def ffffff(gangadhar):
    def saktiman(*args):
        print("****")
        result = gangadhar(*args)
        print(result)
        print("####")
        return result
    return saktiman

# modified_my_sum = ffffff(my_sum)
# modified_cube = ffffff(cube)

def my_deco(anyfunc):
    def wrapper(*args, **kwargs):
        result = f'Result of {", ".join(map(str, args))} is {anyfunc(*args)}'
        return result
    return wrapper


def cube(x):
    return x**3
@my_deco
def my_sum(*args):
    result = 0
    for item in args:
        result += item
    return result

#cube = my_deco(cube)
# my_sum = my_deco(my_sum)

if __name__ == '__main__':
    a = 10
    b = 20
    c = 30
    #print(my_sum(a, b, c))
   # print(modified_my_sum(a, b, c))
    msg = "Sapna"
    
    print(cube(3)) # 27
    # print(my_cube(3)) # "Cube of 3 is 27"
    print(my_sum(a,c,b))


    #print(cube(3))
    # print(modified_cube(3))
    # ffffff(cube)(4)
    