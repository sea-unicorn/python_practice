f = open('../data/50digit.txt')
my_sum = 0
for item in f.readlines():
    my_sum += int(item)
f.close()
print 'First 10 digits of a sum is: ',str(my_sum)[:10]