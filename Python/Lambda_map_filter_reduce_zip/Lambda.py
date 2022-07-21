'''
anonymous function with execution in one line
'''

my_sum = lambda x,y: x+y
print(my_sum(10,30))

is_odd = lambda x: x%2 !=0
print(is_odd(4))

cube = lambda x: x**3

#if odd return square , if even return cube
def compute_value(num: int) -> int:
    if num%2 != 0:
        result = num ** 2
    else:
        result = num ** 3

    return result

print(compute_value(2))

#OR you can write if else in One line
num = 2
result  = num ** 2 if num%2 != 0 else num ** 3
print(result)

#LAMBDA

compute_value_lambda = lambda num: num ** 2 if num%2 != 0 else num ** 3
print(compute_value_lambda(3))




