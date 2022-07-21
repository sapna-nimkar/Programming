'''
reduce 
'''
import functools

nums = [n for n in range(10)]
nums = [1, 2, 3, 4, 5]

# result = 10
# for y in nums:
#     result = x + result

my_sum = functools.reduce(lambda result, y: result+y if y%2 !=0 else result, nums)

print(my_sum)