from factors import Factor
triangle_factors = set()
triangle_number = 1
i = 1
while len(triangle_factors) < 500:
    i += 1
    triangle_number += i
    MyFactor = Factor(triangle_number)
    triangle_factors = MyFactor.get_factors()
    print i, triangle_number,len(triangle_factors)
print 'Smallest triangle number to have more than 500 factors is:' ,triangle_number