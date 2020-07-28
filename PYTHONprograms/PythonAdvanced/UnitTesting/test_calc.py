import unittest
import Basic


class Calc(unittest.TestCase):

    def test_add(self):  # method should start with test
        result = Basic.Add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(Basic.Add(15, 15), 30)

    def test_sub(self):  # method should start with test
        result = Basic.Sub(10, 5)
        self.assertEqual(result, 5)
        self.assertEqual(Basic.Sub(15, 15), 1)

    def test_mul(self):  # method should start with test
        result = Basic.Mul(10, 5)
        self.assertEqual(result, 50)
        self.assertEqual(Basic.Mul(15, 15), 225)

    def test_div(self):  # method should start with test
        result = Basic.Divide(10, 5)
        self.assertEqual(result, 2)

        # To check for the error raise use context manager
        with self.assertRaises(ZeroDivisionError):
            Basic.Divide(10, 0)


# to test in terminal
# >python -m unittest test_calc.py


# for operations before and after the tests
# the methods
# setup() for operations before the tsts
# teardown() for operations after the tests is used

# and even class can be used

# to test in the editor in directly
if __name__ == '__main__':
    unittest.main()

#Mocking
'''
if there is problem in the web and the code is very much fine then this 
but as using the assert depends on the success of the website

To avoid this we use moking

'''
