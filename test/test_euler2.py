import unittest
from sys import path
path.insert(0,'../code')
from euler2_even_fib import Fibonacci

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.treshold = 4000000
        self.result = 4613732

    def test_sum(self):
        MyFibonacci = Fibonacci(self.treshold)
        assert(MyFibonacci.sum() == self.result)

if __name__ == '__main__':
    unittest.main()
