from math import sqrt
for a in xrange(1,250):
    for b in xrange(500-a,500):
        c = sqrt(a*a+b*b)
        if a+b+c == 1000:
            print a,b,c,a*b*c