f=open('../data/1000digit.txt')
my_long_number = f.read().replace('\n','')
digit_prod = long(1)
max_prod = long(1)
numbers = ''
i=0
while i < (1000-12):
    print my_long_number[i:i+13]
    if my_long_number[i+12] == '0':
        i+= 13
    else:
        digit_prod = 1
        for j in xrange(i,i+13):
            digit_prod *= long(my_long_number[j])
        print digit_prod
        if digit_prod > max_prod:
            max_prod = digit_prod
            numbers = my_long_number[i:i+13]
        i+=1
print '13 digits: ', numbers, 'have highest product of: ', max_prod