'''
fibonacci = 0,1,1,2,3,5,8,13....
'''
#recursive: needs to provide info of what values we already know
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#iterative:
def fib_iterate(n):
    results = {0: 0, 1: 1}
    for i in range(2, n+1):
        result = results[i-1] + results[i-2]
        results[i] = result
    return results[n]

print(fib(6))
print(fib_iterate(6))
