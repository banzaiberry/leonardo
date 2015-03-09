# -*- encoding: utf-8 -*-

NLOOP = 10000
PARI_FILE = 'pari.txt'
DISPARI_FILE = 'dispari.txt'

if __name__ == '__main__':

    print "Divide in pari e dispari i numeri e crea due file:'dispari.txt' e 'pari.txt'"

    foPari = open(PARI_FILE,'w')
    foDispari = open(DISPARI_FILE,'w')

    for i in range(0,NLOOP):
        if i % 2 == 0:
            foPari.write("%d\n"%i)
        else:
            foDispari.write("%d\n"%i)


    foPari.close()
    foDispari.close()
    print "Finito"
