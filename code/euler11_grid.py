f = open('../data/grid.txt')
mygrid = []
for line in f.readlines():
    mygrid.append([int(i) for i in line.strip('\n').split(' ')])
f.close()
max_prod = 1
for i in xrange (0,len(mygrid[0])-4):
    for j in xrange(0,len(mygrid)):
        max_prod = max(max_prod,mygrid[i][j]*mygrid[i+1][j]*mygrid[i+2][j]*mygrid[i+3][j])
        if j>2:
            max_prod = max(max_prod,mygrid[i][j]*mygrid[i+1][j-1]*mygrid[i+2][j-2]*mygrid[i+3][j-3])
        if j<(len(mygrid)-4):
            max_prod = max(max_prod,mygrid[i][j]*mygrid[i+1][j+1]*mygrid[i+2][j+2]*mygrid[i+3][j+3])
            max_prod = max(max_prod,mygrid[i][j]*mygrid[i][j+1]*mygrid[i][j+2]*mygrid[i][j+3])
print 'Largest product of 4 adjacent numbers in a grid is:', max_prod