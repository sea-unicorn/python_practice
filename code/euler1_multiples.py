class Multiples():
    def __init__(self,treshold,multiple1,multiple2):
        self.treshold = treshold
        self.multiple1 = multiple1
        self.multiple2 = multiple2
        self.__number_map = [False]*treshold
        self.total = 0

    def sum(self):
        for i in xrange(0,self.treshold,self.multiple1):
            self.__number_map[i] = True
            self.total += i
        for i in xrange(0,self.treshold,self.multiple2):
            if not self.__number_map[i]:
                self.total += i
                self.__number_map[i] = True
        return self.total


def main():
    MyMultiple = Multiples(1000,3,5)
    print MyMultiple.sum()

if __name__ == '__main__':
    main()
