sum = long(0)
sum_of_sq = long(0)

for i in xrange (101):
    sum += i
    sum_of_sq += i*i

difference = sum*sum - sum_of_sq

print 'Difference is ',difference
