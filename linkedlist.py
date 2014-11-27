# 12345 44827 45439 94485

import urllib2
import re

if __name__ == "__main__":
    #first_nothing = "12345"
    first_nothing = "8022"
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % first_nothing
    text = urllib2.urlopen(url).read(10000)
    print text
    nothing = re.search("(and the next nothing is )([0-9]+)", text).group(2)
    print nothing

    for x in range(0, 400):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing
        text = urllib2.urlopen(url).read(10000)
        nothing = re.search("(and the next nothing is )([0-9]+)", text).group(2)

        print nothing
