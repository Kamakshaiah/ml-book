import random
    
def createFactor(cats=['male', 'female'], n=10):
    cats = cats*n
    out = random.sample(cats, n)
    return out

def createVector(start=1, end=10, n=10, m=1, Type=None):
    if Type=='linear':
        out = list(range(n))
    elif Type=='random':
        out = [random.uniform(start, end)*m for i in range(n)]
    else:
        out = [random.randint(start, end)*m for i in range(n)]
    return out

if __name__ == '__main__':
##    resp = createFactor(['yes', 'no'], 10)
##    print(resp)
##    resp = createVector(1, 2, m=100, Type='random')
##    print(resp)
    resp = createVector(1, 2)
    print(resp)
