def collatz(n):
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        length += 1
    return length   
max_length = 0
max_n = 0
for i in xrange(1,1000000,2):
    cur_length = collatz(i)+1
    if max_length < cur_length:
        max_length = cur_length
        max_n = i
print 'Longest sequence length is:',max_length,'number is:', max_n