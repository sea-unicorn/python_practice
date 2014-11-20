import unittest
from sys import path

path.insert(0,'../code')
from euler1_multiples import Multiples

class TestMultiples(unittest.TestCase):
    def setUp(self):
        self.treshold10 = 10
        self.treshold1000 = 1000
        self.multiple1 = 3
        self.multiple2 = 5

    def test10(self):
        MyMultiple10 = Multiples(self.treshold10,self.multiple1,self.multiple2)
        assert(MyMultiple10.sum() == 23)

    def test1000(self):
        MyMultiple1000 = Multiples(self.treshold1000,self.multiple1,self.multiple2)
        assert(MyMultiple1000.sum() == 233168)

if __name__ == '__main__':
    unittest.main()
