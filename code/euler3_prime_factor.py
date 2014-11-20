my_number = 600851475143
i = 2
while i < my_number:
    if my_number%i == 0:
        my_number = my_number/i
    else: i+=1
print 'Largest prime factor is', my_number
