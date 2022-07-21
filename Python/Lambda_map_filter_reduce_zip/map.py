'''
used in iterators (eg. jisko for loop me iterate kar sakte h = list, set, dict, tuple) to compute expression on every element

size of list will remain same Before and After execution, values may change
'''

nums = [i for i in range(10)]

square_nums = [i**2 for i in nums]

def square(n):
    return n**2

square_nums = map(lambda n: n**2 if n%2 != 0 else n**3, nums)
print(square_nums)
for n in square_nums:
    print(n)