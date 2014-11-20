class Factor():
    def __init__(self,number):
        self.number = number
        self.factors = set()
        
    def get_factors(self):
        i = 1
        self.factors = set()
        while i*i<=self.number:
            if self.number%i == 0:
                self.factors.add(i)
                self.factors.add(self.number/i)
            i+=1
        return self.factors