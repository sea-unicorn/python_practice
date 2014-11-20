import unittest
from sys import path

path.insert(0,'../code')
from binary_search import BinarySearch


class Test_BinarySearch(unittest.TestCase):
    def setUp(self):
        self.mystring = 'ABCDEFGLMNOPQ'
        self.myvalue_true = 'A'
        self.myvalue_false = 'J'
    def test_true(self):
        mysearch = BinarySearch(self.mystring,self.myvalue_true)
        assert mysearch.search() == True
    def test_false(self):
        mysearch = BinarySearch(self.mystring,self.myvalue_false)
        assert mysearch.search() == False

if __name__ == '__main__':
    unittest.main()
