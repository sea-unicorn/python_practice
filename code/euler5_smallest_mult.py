smallest_mult = 2 
next = 0
for i in xrange(3,20):
    if smallest_mult % i != 0:
        next = i
        j = 2
        while j < next:
            if next % j == 0:
                next /= j 
            else: j += 1
        smallest_mult *= next

print 'Smallest common multiple of numbers from 1 to 20 is', smallest_mult
