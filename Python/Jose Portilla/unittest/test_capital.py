import unittest
import capital

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = capital.capital_text(text)
        self.assertEqual(result, 'Python')

    def test_two_multiplewords(self):
        text = 'monty python'
        result = capital.capital_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()