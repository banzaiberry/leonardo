# -*- encoding: utf-8 -*-
# Esempio che mostra il costrutto if, elif, else



if __name__ == '__main__':

    # input da tastiera
    inp = raw_input("\nInseririe la temperatura esterna: ")
    temp = int(inp)

    if temp >= 20:
        print "indosso la T-shirt."
    elif temp > 15 and temp < 20:
        print "indosso la felpa."
    elif temp > 5 and temp <= 15:
        print "indosso la maglia di lana."
    elif temp < 5:
         print "indosso il pile."

    inp = raw_input("\nSta piovendo [si/no]? ")
    piove = inp.lower() == 'si'

    inp = raw_input("\nE' prevista pioggia in giornata [si/no]? ")
    previstaPioggia = inp.lower() == 'si'

    if piove or previstaPioggia:
        print "prendo l'ombrello."
    else:
        print "non serve l'ombrello"

