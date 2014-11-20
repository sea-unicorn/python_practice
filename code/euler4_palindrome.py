maxnum = 0
for i in xrange(100,1000):
    for j in xrange(100,1000):
        if str(i*j) == str(i*j)[::-1]:
            maxnum = max(maxnum,i*j)
print 'Found largest palyndrome', maxnum
