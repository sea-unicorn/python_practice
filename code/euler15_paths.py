def factorial(n):
    result = 1
    for i in xrange(1,n+1):
        result *= i
    return result

def combination(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print 'Number of possible paths is:',combination(40,20)