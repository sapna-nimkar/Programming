#Write a function for fibonacci series
#n is the nth place you want to find the fibonacci for
#Concept of Recursion (bottom to top approach)
import unittest


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fib(n-1) + fib(n-2)
    
    return result


def fib(n, results):
    if n == 0:
        results[0] = 0
        return 0
    if n == 1:
        results[1] = 1
        return 1
    result = fib(n-1) + fib(n-2)
    results[n] = result
    return result

results = {}
fib(10, results)

data = {}
def fib_iterative(n):
    results = {0: 0, 1: 1}
    for i in range(2, n+1):
        result = results[i-1] + results[i-2]
        results[i] = result
    return results[n]

class TestFib(unittest.TestCase):
    def test_fib(self):
        n = 5
        expected = 5
        actual = fib(n)
        self.assertEqual(expected, actual, 'Fib function failed')

if __name__ == '__main__':
    print(fib(6))
    print(fib_iterative(6))
    unittest.main()
