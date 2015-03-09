# -*- encoding: utf-8 -*-

NLOOP = 100
if __name__ == '__main__':

    print "Divide in pari e dispari i numeri"

    for i in range(0,NLOOP):
        if i % 2 == 0:
            print "%d è pari"%i
        else:
            print "%d è dispari"%i