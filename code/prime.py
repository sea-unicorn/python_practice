class PrimeNumbers():
    def __init__(self,treshold):
        self.treshold = treshold
        self.prime_map = [False]+[False]+[True]*(self.treshold-2)
        self.pointer = 2 
        self.prime_num_set = set()
        self.prime_num_list = []

    def generate(self):
        while self.pointer < self.treshold:
            for i in xrange(self.pointer*2,self.treshold,self.pointer):
                self.prime_map[i] = False
            for i in xrange(self.pointer+1,self.treshold):
                if self.prime_map[i]: 
                    self.pointer = i
                    break
                self.pointer=self.treshold
        return self.prime_map

    def get_set(self):
        self.generate()
        for i,item in enumerate(self.prime_map):
            if item: self.prime_num_set.add(i)
        return self.prime_num_set

    def get_list(self):
        self.generate()
        for i,item in enumerate(self.prime_map):
            if item: self.prime_num_list.append(i)
        return self.prime_num_list

