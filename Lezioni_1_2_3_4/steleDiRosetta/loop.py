# -*- encoding: utf-8 -*-
#Esempio che mostra il loop e le chiamate a finzioni esterne

import math
import time


NLOOP=1000000;


if __name__ == '__main__':

    print "Begin loop"

    start = time.time()*1000.0

    for i in range(0,NLOOP):
        p2 = long(math.pow(i,2.0))
        p3 = long(math.pow(i,3.0))
        sq = math.sqrt(i)
        print "%d\t%d\t%d\tRADICE:%5.3f"%(i,p2,p3,sq)
        print "-"*80
        #print "ho sonno vado a dormire"
        #time.sleep(3)
        #print "mi sono svegliato"

    print "End loop"
    stop = time.time()*1000.0
    time_spent = stop - start
    print "Done in %3.2f millsec"%time_spent