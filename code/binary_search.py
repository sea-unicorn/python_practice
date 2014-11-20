#!/bin/python
class BinarySearch:
    def __init__(self,mystring,myvalue):
        self.mystring = mystring
        self.myvalue = myvalue
        self.__length = 0
        self.__myitem = ''
    def search(self):
        self.__length = len(self.mystring)
        self.__myitem = self.mystring[self.__length/2]
        if self.__myitem == self.myvalue:
            print 'found'
            return True
        elif self.__length == 1:
            print 'Not found'
            return False
        elif self.__myitem < self.myvalue:
            self.mystring = self.mystring[self.__length/2:]
            print 'looking at',self.mystring
            return self.search()
        else:
            self.mystring = self.mystring[:self.__length/2]
            print 'looking at', self.mystring
            return self.search()


def main():
    mysearch = BinarySearch('ABCDEFG','J')
    print mysearch.search()

if __name__ == '__main__':
    main()
