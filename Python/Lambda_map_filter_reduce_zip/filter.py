'''
help in filtering ther items, will NOT do any operations on them
'''

nums = [x for x in range(10)]

odd_nums = list(filter( lambda x: x%2 != 0, nums))
print(odd_nums)

5 % 2 != 0 # True
4 % 2 != 0 # False

