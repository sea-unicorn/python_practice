from prime import PrimeNumbers
MyPrime = PrimeNumbers(2000000)
sum_of_primes = 0
for item in MyPrime.get_set():
    sum_of_primes += item
print 'Sum of all primes below 2 million is: ',sum_of_primes