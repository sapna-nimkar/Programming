#find factorial of a particular number n
#using iterative method
#using recursion

#iterative method

import unittest
import count_letters

def fact_iterative(n):
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

def fact_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fact_recursive(n-1)

class TestFactorial(unittest.TestCase):
    def test_fact_recur(self):
        n = 5
        expected = 120
        actual = fact_recursive(n)
        self.assertEqual(expected, actual, 'Factorial failed')
    def test_fact_iter(self):
        n = 5
        expected = 120
        actual = fact_iterative(n)
        self.assertEqual(expected, actual, 'Iter Factorial Failed')


if __name__ == '__main__':
    unittest.main()
