class Fibonacci():
    def __init__(self,treshold):
        self.treshold = treshold
        self.prev = 0
        self.next = 1
        self.total = 0

    def sum(self):
        while self.next <= self.treshold:
            if self.next%2 == 0:
                self.total+=self.next
            self.prev,self.next = self.next,self.prev+self.next
        return self.total

def main():
    MyFibonacci = Fibonacci(4000000)
    print MyFibonacci.sum()

if __name__ == '__main__':
    main()
