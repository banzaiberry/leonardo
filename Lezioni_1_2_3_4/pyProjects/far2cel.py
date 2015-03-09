# -*- encoding: utf-8 -*-
#Esempio che mostra come si defiiscono le funzioni

import math
import time

#°C = (°F − 32) / 1,8
def far2cel(inF):
    outC = float(inF - 32)/1.8
    return outC



if __name__ == '__main__':

    print "Convertitore Fahrenheit --> Celsius"
    inF = 100
    outC = far2cel(inF)
    print "%d gradi Fahrenheit equivalgono a %5.3f gradi Celsius"%(inF,outC)

    # input da tastiera
    print "Premi q per uscire."
    while True:

        num = str(raw_input("\nInseririe i gradi Fahrenheit: "))
        if num == 'q':
            print "ciao ciao"
            break

        try:
            inF = int(num)
            outC = far2cel(inF)
            print "%d gradi Fahrenheit equivalgono a %5.3f gradi Celsius\n"%(inF,outC)
        except Exception,e:
            print "ERRORE: non è stato inserito un numero"



