from sys import stdout
def check_anagrams(first_words, second_words):
    for i in xrange(len(first_words)):
        first_word = first_words[i]
        second_word = second_words[i]
        success = 1
        for letter in first_word:
            if second_word.find(letter) == -1:
                success = 0
                break
            else:
                second_word = second_word.replace(letter,'',1)
        stdout.write(str(success))
        

def maxdiff(v):
    maxdiff = 0
    for b in xrange(len(v)):
        for i in xrange(b+1,len(v)):
            for j in xrange(i+1,len(v)):
                for e in xrange(j+1,len(v)):
                    maxdiff = max(sum(v[j:e+1])-sum(v[b:i+1]),maxdiff)
    stdout.write(str(maxdiff))
    
def find_deviation(v, d):
    deviation = 0
    for i in xrange(len(v)-d+1):
        deviation = max(max(v[i:i+d])-min(v[i:i+d]),deviation)
    stdout.write(str(deviation))
              
find_deviation([6, 9, 4, 7, 4, 1],3)
check_anagrams(["cinema","host","abba","train"],["iceman","shot","bab","rain"])
maxdiff( [3, -5, 1, -2, 8, -2, 3, -2, 1])