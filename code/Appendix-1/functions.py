import random
import math
import statistics as sts

def mean(x):
    return sum(x)/len(x)

def variance(x):
    n = len(x)
    am = mean(x)
    return sum((x - am) ** 2 for x in x) / (n - 1)

def stdev(x):
    res = variance(x)
    return math.sqrt(res)

if __name__ == '__main__':
        
    data_x  = [random.randint(10, 100) for i in range(10)]
    print(data_x)
    print(mean(data_x))
    print(sts.mean(data_x))
    print(variance(data_x))
    print(sts.variance(data_x))
    print(stdev(data_x))
    print(sts.stdev(data_x))
