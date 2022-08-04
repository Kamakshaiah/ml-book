import random
import math
import statistics as sts

class summaries():

    data = list()
    
    def __init__(self, data):
        self.data = data
        
    def mean(self):
        return sum(self.data)/len(self.data)

    def variance(self):
        n = len(self.data)
        am = self.mean()
        return sum((i - am) ** 2 for i in self.data) / (n - 1)

    def stdev(self):
        res = self.variance()
        return math.sqrt(res)

if __name__ == '__main__':
        
    x  = [random.randint(10, 100) for i in range(10)]
    summaries = summaries(x)
    print(summaries.mean())
    print(summaries.variance())
    print(summaries.stdev())
